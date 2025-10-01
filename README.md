# LlamaIndex RAG Agent with Streamlit UI

A conversational interface for querying documents using LlamaIndex and OpenAI.

![UI Demo](ui-firstdraft.jpeg)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `data` directory and add your documents:
```bash
mkdir data
# Add your .txt, .pdf, .html, or other documents to the data/ folder
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Configuration

In the sidebar, you can:
- Enter your OpenAI API key
- Select the language model (GPT-4, GPT-3.5, etc.)
- Choose an embedding model
- Adjust the temperature for response creativity
- Rebuild the index if you've added new documents

### Adding Documents

1. Place your documents in the `data/` directory
2. Click "Rebuild Index" in the sidebar (if index already exists)
3. Start asking questions!

## How It Works

1. **Document Loading**: Documents from the `data/` directory are loaded and processed
2. **Indexing**: Text is embedded using OpenAI's embedding models and stored in a vector index
3. **Persistence**: The index is saved to `./storage` for faster subsequent loads
4. **Query**: User questions are embedded and matched against the document index
5. **Response**: Relevant context is retrieved and sent to the LLM to generate answers

## Troubleshooting

- **No documents found**: Make sure you have files in the `data/` directory
- **API errors**: Verify your OpenAI API key is valid and has credits
- **Index issues**: Use the "Rebuild Index" button to recreate the vector store
