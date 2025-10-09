# 🤖 LlamaIndex RAG Chatbot Template

A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on your company's documents using LlamaIndex and OpenAI.

---

## 📋 Table of Contents

- [What This Does](#what-this-does)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Adding Your Data](#adding-your-data)
- [Running Locally](#running-locally)
- [Deploying to Hugging Face](#deploying-to-hugging-face)
- [Embedding in Your Website](#embedding-in-your-website)
- [Troubleshooting](#troubleshooting)

---

## 🎯 What This Does

This chatbot uses **Retrieval-Augmented Generation (RAG)** to answer questions about your documents:

1. **Reads your documents** from the `data/` folder
2. **Creates a searchable index** using AI embeddings
3. **Answers questions** by finding relevant information and generating responses
4. **Remembers conversation context** within each chat session

**Example Use Case**: A customer support chatbot that answers questions about your company's products, policies, or services.

---

## 📁 Repository Structure

```
llama-test/
├── app.py                      # Main Streamlit chatbot application
├── data/                       # Put your documents here (PDF, HTML, TXT, etc.)
│   ├── example_document.pdf
│   └── company_info.html
├── storage/                    # Auto-generated vector database (don't edit)
│   ├── docstore.json
│   ├── index_store.json
│   └── default__vector_store.json
├── requirements.txt            # Python dependencies
├── .env.example               # Template for API key (copy to .env)
├── .gitignore                 # Prevents sensitive files from being committed
├── README.md                  # This file
└── llama_test.ipynb          # (Optional) Learning notebook - not needed for final app
```

**File Purposes**:
- **`app.py`**: The chatbot interface - this is what runs your bot
- **`data/`**: Where you store your company documents
- **`storage/`**: Automatically created cache of indexed documents (speeds up loading)
- **`llama_test.ipynb`**: Tutorial notebook showing how RAG works (optional reference)

---

## ✅ Prerequisites

Before starting, make sure you have:

1. **Python 3.9+** installed ([Download here](https://www.python.org/downloads/))
2. **Git** installed ([Download here](https://git-scm.com/downloads))
3. **An OpenAI API key** ([Get one here](https://platform.openai.com/api-keys))
   - You'll need to add payment info to OpenAI (~$5 credit is sufficient for testing)
4. **A GitHub account** ([Sign up here](https://github.com/signup))
5. **A Hugging Face account** ([Sign up here](https://huggingface.co/join))

---

## 🚀 Setup Instructions

### Step 1: Clone This Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### Step 2: Create a Virtual Environment

**On macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Your API Key

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
   ```

   ⚠️ **Important**: Never commit your `.env` file to GitHub! It's already in `.gitignore`.

---

## 📄 Adding Your Data

### Supported File Types
- PDF documents (`.pdf`)
- HTML files (`.html`)
- Text files (`.txt`)
- Markdown files (`.md`)
- CSV files (`.csv`)

### How to Add Documents

1. Place all your company documents in the `data/` folder
2. The chatbot will automatically read and index them when it starts

**Example**:
```
data/
├── product_catalog.pdf
├── faq.html
├── company_policies.txt
└── pricing_guide.csv
```

### Tips for Better Results
- Use clear, well-formatted documents
- Include relevant information only (avoid irrelevant content)
- Break very large documents into smaller, topic-focused files
- Name files descriptively (e.g., `refund_policy.pdf` not `doc1.pdf`)

---

## 💻 Running Locally

### Start the Chatbot

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### First Run
- The chatbot will read all documents in `data/` and create an index
- This takes 10-30 seconds depending on document size
- A `storage/` folder will be created automatically
- Future runs will be faster because the index is cached

### Testing Your Chatbot
Try asking questions like:
- "What products do you offer?"
- "What is your refund policy?"
- "Tell me about [specific topic from your documents]"

---

## 🌐 Deploying to Hugging Face

### Why Deploy?
- Makes your chatbot publicly accessible
- Free hosting for public projects
- Easy to share with your team and embed in websites

### Deployment Steps

1. **Create a new Space** at [huggingface.co/new-space](https://huggingface.co/new-space)
   - Name: `your-company-chatbot`
   - License: Apache 2.0
   - SDK: Streamlit
   - Hardware: CPU Basic (free)

2. **Upload your files**:
   - `app.py`
   - `requirements.txt`
   - `data/` folder with your documents
   - `storage/` folder (optional - will regenerate if missing)

3. **Add your API key as a Secret**:
   - Go to Space Settings → Repository secrets
   - Add: `OPENAI_API_KEY` = `your-key-here`

4. **Wait for build** (2-3 minutes)
   - Check the "Logs" tab for any errors
   - Once running, your chatbot is live!

Your chatbot URL will be: `https://huggingface.co/spaces/YOUR-USERNAME/your-company-chatbot`

---

## 🌍 Embedding in Your Website

Once deployed to Hugging Face, you can embed your chatbot in any HTML page.

### Option 1: Floating Chat Widget (Recommended)

Add this code before the closing `</body>` tag of your HTML:

```html
<!-- Chatbot Widget Styles -->
<style>
  .chat-widget-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    width: 400px;
    height: 600px;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    display: none;
  }

  .chat-widget-container.open {
    display: block;
  }

  .chat-widget-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  }

  .chat-widget-button:hover {
    transform: scale(1.1);
  }

  @media (max-width: 768px) {
    .chat-widget-container {
      width: calc(100vw - 40px);
      height: calc(100vh - 140px);
    }
  }
</style>

<!-- Chatbot Toggle Button -->
<button class="chat-widget-button" onclick="toggleChat()">💬</button>

<!-- Chatbot Container -->
<div class="chat-widget-container" id="chatWidget">
  <iframe 
    src="https://huggingface.co/spaces/YOUR-USERNAME/your-company-chatbot"
    width="100%" 
    height="100%" 
    frameborder="0">
  </iframe>
</div>

<!-- Toggle Script -->
<script>
  function toggleChat() {
    const widget = document.getElementById('chatWidget');
    const button = document.querySelector('.chat-widget-button');
    
    if (widget.classList.contains('open')) {
      widget.classList.remove('open');
      button.textContent = '💬';
    } else {
      widget.classList.add('open');
      button.textContent = '✕';
    }
  }
</script>
```

### Option 2: Full-Page Embed

```html
<iframe 
  src="https://huggingface.co/spaces/YOUR-USERNAME/your-company-chatbot"
  width="100%" 
  height="600px" 
  frameborder="0">
</iframe>
```

**Important**: Replace `YOUR-USERNAME/your-company-chatbot` with your actual Space URL!

---

## 🔧 Troubleshooting

### "Please add documents to the 'data' directory"
- Make sure you have files in the `data/` folder
- Check that files are in supported formats (PDF, HTML, TXT, etc.)

### "OPENAI_API_KEY not found"
- Check that your `.env` file exists and contains the key
- On Hugging Face: verify the secret is set in Settings → Repository secrets

### Chatbot gives wrong answers
- Make sure your documents contain the relevant information
- Try rephrasing your question more specifically
- Check if the document text is readable (not corrupted or image-only PDFs)

### "Module not found" error
- Run `pip install -r requirements.txt` again
- Make sure your virtual environment is activated

### Slow response times
- First query after starting is always slower (building index)
- Subsequent queries should be faster (using cached index)
- On Hugging Face, free tier may be slower during peak times

### Storage folder issues
- Delete the `storage/` folder and restart - it will regenerate
- This forces a fresh index of your documents

---

## 📚 Additional Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)

---

## 📝 Project Integration

This chatbot template is designed for the ENGCMP 0600 project:

- **Steps 6-7**: Add your company documents to `data/`
- **Steps 7-9**: Test and refine your chatbot locally
- **Step 8**: Deploy to Hugging Face Spaces
- **Step 8**: Embed in your company website using the iframe code
- **Step 10**: Present your working chatbot as part of your final demo

---

## 🤝 Support

If you run into issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review your code against this README
3. Check Hugging Face Space logs for error messages
4. Ask your instructor or TA for help

---

**Good luck building your AI-powered chatbot! 🚀**