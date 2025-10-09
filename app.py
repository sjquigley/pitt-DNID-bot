import streamlit as st
import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Load environment variables from .env (if present)
load_dotenv()

# Backend configuration (from llama_test.ipynb)
# These values are fixed and cannot be changed from the UI
LLM_MODEL = "gpt-5-nano-2025-08-07"
EMBEDDING_MODEL = "text-embedding-3-small"
TEMPERATURE = 0.1
DATA_DIR = "data"
PERSIST_DIR = "./storage"

# Configure Streamlit page
st.set_page_config(
    page_title="LlamaIndex RAG Agent",
    page_icon="🦙",
    layout="centered"
)
# Get API key from environment variable or Streamlit secrets
# This should be set before running the Streamlit app
openai_api_key = os.getenv('OPENAI_API_KEY') or st.secrets.get("OPENAI_API_KEY")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize query engine
@st.cache_resource
def initialize_query_engine(_api_key):
    """Initialize the LlamaIndex query engine with caching"""

    # Set API key
    os.environ['OPENAI_API_KEY'] = _api_key

    # Configure models with backend configuration
    llm = OpenAI(model=LLM_MODEL, temperature=TEMPERATURE)
    embed_model = OpenAIEmbedding(model=EMBEDDING_MODEL)

    try:
        if not os.path.exists(PERSIST_DIR):
            # Load documents and create index
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)
                return None, "Please add documents to the 'data' directory"

            documents = SimpleDirectoryReader(DATA_DIR).load_data()

            if not documents:
                return None, "No documents found in the 'data' directory"

            index = VectorStoreIndex.from_documents(
                documents,
                llm=llm,
                embed_model=embed_model
            )
            # Store for later
            index.storage_context.persist(persist_dir=PERSIST_DIR)
            status = f"✅ Index created with {len(documents)} documents"
        else:
            # Load existing index
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)

            # Configure the loaded index with LLM and embedding models
            # This ensures the query engine uses the correct models
            index._llm = llm
            index._embed_model = embed_model
            status = "✅ Index loaded from storage"

        # Create query engine
        query_engine = index.as_query_engine(llm=llm, embed_model=embed_model)
        return query_engine, status

    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Main chat interface
if not openai_api_key:
    st.warning("⚠️ Please set the OPENAI_API_KEY environment variable to get started.")
    st.stop()

# Initialize query engine
if "query_engine" not in st.session_state:
    with st.spinner("Initializing RAG agent..."):
        query_engine, status = initialize_query_engine(openai_api_key)
        st.session_state.query_engine = query_engine

        if query_engine is None:
            st.error(status)
            st.stop()
        else:
            st.success(status)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your documents"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.query_engine.query(prompt)
                response_text = str(response)
                st.markdown(response_text)

                # Add assistant response to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response_text
                })

            except Exception as e:
                error_msg = f"Error generating response: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
