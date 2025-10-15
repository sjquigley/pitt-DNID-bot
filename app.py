import streamlit as st
import os
import asyncio
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, Document
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_cloud_services import LlamaParse

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

# Get API keys from environment variable or Streamlit secrets
# These should be set before running the Streamlit app
openai_api_key = os.getenv('OPENAI_API_KEY') or st.secrets.get("OPENAI_API_KEY")
llama_cloud_api_key = os.getenv('LLAMA_CLOUD_API_KEY') or st.secrets.get("LLAMA_CLOUD_API_KEY")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Helper function to load documents with LlamaParse
def load_documents_with_llamaparse(data_dir: str, llama_api_key: str) -> List[Document]:
    """
    Load documents from data directory using LlamaParse for complex file types
    and SimpleDirectoryReader for basic text files.

    Supported complex file types: PDF, DOCX, PPTX, XLSX
    """
    data_path = Path(data_dir)
    if not data_path.exists():
        return []

    # File extensions that benefit from LlamaParse
    llamaparse_extensions = {'.pdf', '.docx', '.pptx', '.xlsx', '.doc', '.ppt', '.xls'}
    # File extensions for simple text reading
    simple_extensions = {'.txt', '.md', '.csv', '.json', '.html', '.xml'}

    all_files = list(data_path.glob('*'))
    llamaparse_files = []
    simple_files = []

    for file_path in all_files:
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext in llamaparse_extensions:
                llamaparse_files.append(str(file_path))
            elif ext in simple_extensions:
                simple_files.append(str(file_path))

    documents = []

    # Process complex files with LlamaParse
    if llamaparse_files:
        st.info(f"📄 Processing {len(llamaparse_files)} complex file(s) with LlamaParse: {', '.join([Path(f).name for f in llamaparse_files])}")
        try:
            # Configure LlamaParse with optimal settings
            parser = LlamaParse(
                api_key=llama_api_key,
                parse_mode="parse_page_with_agent",
                model="openai-gpt-4-1-mini",
                high_res_ocr=True,
                adaptive_long_table=True,
                outlined_table_extraction=True,
                output_tables_as_HTML=True,
                num_workers=4,
                verbose=True,
                language="en"
            )

            # Parse files (LlamaParse handles batch processing)
            # Use asyncio to run the async parse method
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                if len(llamaparse_files) == 1:
                    result = loop.run_until_complete(parser.aparse(llamaparse_files[0]))
                    results = [result]
                else:
                    results = loop.run_until_complete(parser.aparse(llamaparse_files))
            finally:
                loop.close()

            # Convert JobResults to LlamaIndex Documents
            for result in results:
                # Get markdown documents with page splitting for better chunking
                llamaparse_docs = result.get_markdown_documents(split_by_page=True)
                documents.extend(llamaparse_docs)

        except Exception as e:
            st.warning(f"LlamaParse processing failed for some files: {str(e)}")
            st.info("Falling back to SimpleDirectoryReader for these files...")
            # Fall back to simple reader if LlamaParse fails
            simple_files.extend(llamaparse_files)

    # Process simple text files with SimpleDirectoryReader
    if simple_files:
        st.info(f"📝 Processing {len(simple_files)} simple file(s) with SimpleDirectoryReader: {', '.join([Path(f).name for f in simple_files])}")
        for file_path in simple_files:
            try:
                file_docs = SimpleDirectoryReader(input_files=[file_path]).load_data()
                documents.extend(file_docs)
            except Exception as e:
                st.warning(f"Failed to load {file_path}: {str(e)}")

    return documents

# Initialize query engine
@st.cache_resource
def initialize_query_engine(_openai_api_key, _llama_api_key):
    """Initialize the LlamaIndex query engine with caching"""

    # Set API keys
    os.environ['OPENAI_API_KEY'] = _openai_api_key
    if _llama_api_key:
        os.environ['LLAMA_CLOUD_API_KEY'] = _llama_api_key

    # Configure models with backend configuration
    llm = OpenAI(model=LLM_MODEL, temperature=TEMPERATURE)
    embed_model = OpenAIEmbedding(model=EMBEDDING_MODEL)

    try:
        if not os.path.exists(PERSIST_DIR):
            # Load documents and create index
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)
                return None, "Please add documents to the 'data' directory"

            # Use LlamaParse if API key is available, otherwise fall back to SimpleDirectoryReader
            if _llama_api_key:
                st.info("Using LlamaParse for advanced document processing...")
                documents = load_documents_with_llamaparse(DATA_DIR, _llama_api_key)
            else:
                st.info("Using SimpleDirectoryReader (LlamaParse API key not found)...")
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

# Display info about LlamaParse availability
if not llama_cloud_api_key:
    st.info("💡 Tip: Set LLAMA_CLOUD_API_KEY to enable advanced parsing of PDFs, DOCX, and other complex documents.")

# Initialize query engine
if "query_engine" not in st.session_state:
    with st.spinner("Initializing RAG agent..."):
        query_engine, status = initialize_query_engine(openai_api_key, llama_cloud_api_key)
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
