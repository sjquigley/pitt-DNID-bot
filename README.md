# 🤖 LlamaIndex RAG Chatbot Template

![final product demo](example/visuals/embeddedui-demo.png)

A Retrieval-Augmented Generation (RAG) chatbot template that answers questions based on your company's documents using LlamaIndex and OpenAI.

> **📘 For Students**: This is a template for your project. The main folder contains your workspace, and the `examples/` folder shows a complete working version for reference.

---

## 📋 Table of Contents

- [Repository Structure](#-repository-structure)
- [What This Does](#-what-this-does)
- [Prerequisites](#-prerequisites)
- [Setup Instructions](#-setup-instructions)
- [Adding Your Data](#-adding-your-data)
- [Development & Testing Options](#-development--testing-options)
- [Testing with the Example](#-testing-with-the-example)
- [Deploying to Hugging Face](#-deploying-to-hugging-face)
- [Embedding in Your Website](#-embedding-in-your-website)
- [Publishing to GitHub Pages](#-publishing-your-website-to-github-pages)
- [Troubleshooting](#-troubleshooting)
- [Project Integration](#-project-integration-engcmp-0600)
- [Recommended Workflow](#-recommended-workflow)

---

## 📁 Repository Structure

```
llama-chatbot-template/
├── README.md                    # ← You are here!
├── .env.example                 # Template for your API key
├── .gitignore                   # Protects sensitive files
├── requirements.txt             # Python dependencies
├── app.py                       # YOUR chatbot (work here!)
├── data/                        # YOUR documents go here (currently empty)
│   └── README.md
│
└── examples/                    # 👀 Reference only
    ├── llama_test.ipynb         # Learning notebook for Colab
    ├── index.html         # Full website (HTML, CSS, JS) saved locally w/ embedded chatbot script
    ├── data/                    # Example documents
    │   ├── taylor_swift_biography.html
    │   └── constitution.pdf
    └── storage/                 # Pre-built index for example
```

### 🎯 Where to Work

- **`app.py`** - Your main chatbot code (already complete, no edits needed!)
- **`data/`** - Put YOUR company documents here
- **`examples/`** - Look here if you get stuck (don't edit this!)

### 📂 What Gets Created

When you run the app, it will automatically create:
- **`storage/`** - Cached index of your documents (speeds up loading)

---

## 🎯 What This Does

This chatbot uses **Retrieval-Augmented Generation (RAG)** to answer questions about your documents:

1. **📖 Reads your documents** from the `data/` folder
2. **🔍 Creates a searchable index** using AI embeddings
3. **💬 Answers questions** by finding relevant information and generating responses
4. **🧠 Remembers conversation** context within each chat session

**Example Use Case**: A customer support chatbot that answers questions about your company's products, policies, or services.

---

## ✅ Prerequisites

Before starting, make sure you have:

1. **A Google account** for Google Colab ([Sign up here](https://accounts.google.com/signup))
2. **Google Colab Pro (FREE for students!)** ([Get it here](https://colab.research.google.com/signup/pricing))
   - ✨ Faster execution
   - ⏱️ Longer runtime limits
   - 💾 More storage
   - ⚡ Priority access to GPUs
   - 🎓 **100% FREE with your .edu email** - verification takes ~2 seconds!
3. **An OpenAI API key** 
   - 🎓 **Your instructor will provide a shared API key** for the class
   - No payment required! Use the key provided by your instructor
   - (Alternative: Get your own at [platform.openai.com/api-keys](https://platform.openai.com/api-keys) with ~$5 credit)
4. **A GitHub account** ([Sign up here](https://github.com/signup))
5. **A Hugging Face account** ([Sign up here](https://huggingface.co/join)) - for deployment

---

## 🚀 Setup Instructions

### Step 1: Create Your Google Colab Account

1. Go to [Google Colab](https://colab.research.google.com/)
2. Sign in with your Google account
3. **Get Colab Pro for FREE**:
   - Go to [Colab Pro pricing page](https://colab.research.google.com/signup/pricing)
   - Click "Get Colab Pro" and verify with your .edu email
   - Instant approval! No payment required for students 🎉
   - Enjoy faster runtimes and priority access

### Step 2: Fork This Repository

1. Go to the repository on GitHub
2. Click the "Fork" button in the top right
3. This creates your own copy of the project

### Step 3: Connect Colab to Your GitHub

1. In Google Colab, click **File → Open notebook**
2. Select the **GitHub** tab
3. Enter your repository URL or search for your username
4. Open `examples/llama_test.ipynb` to start learning!

### Step 4: Set Up Your OpenAI API Key in Colab

**Option A: Using Colab Secrets (Recommended)**

1. In your Colab notebook, click the 🔑 key icon in the left sidebar
2. Click "Add new secret"
3. Name: `OPENAI_API_KEY`
4. Value: `sk-proj-xxxxxxxxxxxxxxxxxxxxx` (your actual key)
5. Toggle "Notebook access" to ON

**Option B: Using Code (Less Secure)**

```python
from google.colab import userdata
import os

# This retrieves your secret key
os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
```

⚠️ **Important**: Never hardcode your API key directly in the notebook!

---

## 📄 Adding Your Data

### Supported File Types
- PDF documents (`.pdf`)
- HTML files (`.html`)
- Text files (`.txt`)
- Markdown files (`.md`)
- CSV files (`.csv`)

### How to Add Documents to Colab

**Method 1: Upload Directly (Quick Testing)**

1. In your Colab notebook, run:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
2. Select your documents to upload
3. Files will be in the current directory

**Method 2: Mount Google Drive (Recommended)**

1. Upload your documents to a folder in Google Drive (e.g., `My Drive/chatbot-data/`)
2. In your Colab notebook:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Access files from: `/content/drive/MyDrive/chatbot-data/`

**Method 3: Push to GitHub (For Deployment)**

1. Add your documents to the `data/` folder in your repository
2. Commit and push to GitHub
3. Pull the repository in Colab or deploy directly to Hugging Face

### Tips for Better Results
- ✅ Use clear, well-formatted documents
- ✅ Include only relevant company information
- ✅ Break very large documents into smaller, topic-focused files
- ❌ Don't include sensitive data (passwords, private info)
- ❌ Avoid image-only PDFs (text must be selectable)

---

## 🧪 Development & Testing Options

You have **two options** for developing and testing your chatbot. Choose the one that works best for you!

---

### 🌐 Option 1: Google Colab (Recommended for Beginners)

**Pros**: No installation needed, works in browser, free GPU access
**Cons**: Temporary URLs, session expires after inactivity

**Use this if**: You prefer browser-based development or don't want to install Python locally

---

### 💻 Option 2: Local Development (Recommended for Advanced Users)

**Pros**: Persistent environment, faster development, works offline
**Cons**: Requires Python installation and setup

**Use this if**: You're comfortable with terminal/command line and want full control

---

## 🌐 Option 1: Testing in Google Colab

### Phase 1: Learning with the Example Notebook

The example notebook (`examples/llama_test.ipynb`) teaches you RAG concepts interactively.

1. **Open the example notebook** in Colab:
   - Go to your forked repository
   - Navigate to `examples/llama_test.ipynb`
   - Click "Open in Colab" badge (or manually open via Colab)

2. **Install dependencies** (First cell - run this first!):
   ```python
   # STEP 1: Install all required packages
   print("📦 Installing dependencies...")
   
   !pip install -q streamlit==1.50.0
   !pip install -q llama-index==0.14.4
   !pip install -q llama-index-core==0.14.4
   !pip install -q llama-index-llms-openai==0.6.4
   !pip install -q llama-index-embeddings-openai==0.5.1
   !pip install -q openai==1.109.1
   !pip install -q python-dotenv==1.1.1
   !pip install -q jedi==0.19.2
   
   print("✅ All dependencies installed!")
   ```
   ⏱️ This takes 1-2 minutes. Wait for "✅ All dependencies installed!" before continuing.

3. **Set up your API key** (Second cell):
   ```python
   # STEP 2: Configure OpenAI API Key
   from google.colab import userdata
   import os
   
   # Get API key from Colab secrets (you must add this first!)
   os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
   print("✅ API key loaded")
   ```

4. **Load and index documents** (Third cell):
   ```python
   # STEP 3: Load documents and create index
   from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
   from llama_index.llms.openai import OpenAI
   from llama_index.embeddings.openai import OpenAIEmbedding
   
   # Configure models
   llm = OpenAI(model="gpt-5-nano-2025-08-07", temperature=0.1)
   embed_model = OpenAIEmbedding(model="text-embedding-3-small")
   
   # Load documents from data folder
   documents = SimpleDirectoryReader("data").load_data()
   print(f"📄 Loaded {len(documents)} documents")
   
   # Create searchable index
   index = VectorStoreIndex.from_documents(
       documents,
       llm=llm,
       embed_model=embed_model
   )
   print("✅ Index created successfully!")
   ```

5. **Query the chatbot** (Fourth cell):
   ```python
   # STEP 4: Ask questions!
   query_engine = index.as_query_engine()
   
   # Try your first question
   response = query_engine.query("Your question here")
   print(response)
   ```

6. **Test with example data** first, then replace with your own documents

### Phase 2: Running Your Streamlit App in Colab

Once you understand how RAG works from the notebook, transition to testing your actual `app.py` Streamlit application.

#### Why Transition to app.py?

- 📓 **Notebook (`llama_test.ipynb`)**: Learning tool, shows RAG step-by-step
- 🚀 **Streamlit app (`app.py`)**: Production-ready chatbot with UI, what you'll deploy

#### Step-by-Step: Running app.py in Colab

1. **Create a new Colab notebook** (or add cells to your existing one):
   - File → New notebook
   - Or continue in your existing notebook

2. **Install dependencies** (same as before):
   ```python
   !pip install -q streamlit==1.50.0 llama-index==0.14.4 llama-index-core==0.14.4 llama-index-llms-openai==0.6.4 llama-index-embeddings-openai==0.5.1 openai==1.109.1 python-dotenv==1.1.1 jedi==0.19.2
   ```

3. **Clone your repository** (if not already in Colab):
   ```python
   # Clone your forked repository
   !git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   %cd YOUR-REPO-NAME
   ```

4. **Set up your API key as environment variable**:
   ```python
   import os
   from google.colab import userdata
   
   # Set API key for the app to use
   os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
   ```

5. **Upload your documents** (if not already in the repo):
   ```python
   # Option A: Upload directly to Colab
   from google.colab import files
   uploaded = files.upload()
   # Move uploaded files to data folder
   !mkdir -p data
   !mv *.pdf data/  # Adjust file extensions as needed
   
   # Option B: Mount Google Drive
   from google.colab import drive
   drive.mount('/content/drive')
   !cp -r /content/drive/MyDrive/chatbot-data/* data/
   ```

6. **Install localtunnel to expose Streamlit**:
   ```python
   # Install localtunnel for public URL
   !npm install -g localtunnel
   ```

7. **Run Streamlit in the background**:
   ```python
   # Run Streamlit app in background
   !streamlit run app.py &>/content/logs.txt &
   
   # Wait for Streamlit to start
   import time
   time.sleep(5)
   
   # Verify it's running
   !curl http://localhost:8501
   ```

8. **Expose with localtunnel to get a public URL**:
   ```python
   # Get a public URL using localtunnel
   !npx localtunnel --port 8501 &
   
   # Wait a moment for the URL
   import time
   time.sleep(3)
   
   # The URL will appear in the output above
   # Look for: "your url is: https://xxxxx.loca.lt"
   ```

9. **Access your chatbot**:
   - Click the URL from localtunnel output (looks like `https://xxxxx.loca.lt`)
   - Click "Click to Continue" on the localtunnel page
   - Your Streamlit chatbot interface will appear! 🎉

![chatbot ui demo](example/visuals/ui-demo.jpeg)

10. **Test your chatbot**:
    - Ask questions about your documents
    - Verify responses are accurate
    - Test different types of queries

#### Important Notes for Running app.py in Colab:

⚠️ **Limitations**:
- Localtunnel URLs are temporary (expire when Colab disconnects)
- Not suitable for permanent hosting
- Great for testing and development only

✅ **When to Use This**:
- Testing your app with real documents before deploying
- Showing your team the chatbot interface during development
- Debugging issues before Hugging Face deployment

🚀 **For Production**:
- After testing in Colab, deploy to Hugging Face Spaces (permanent hosting)
- Colab is for **development and testing**
- Hugging Face is for **production and embedding**

#### Workflow Summary:

```
Step 1: Learn RAG concepts
└─→ Use llama_test.ipynb notebook

Step 2: Test with your data
└─→ Add your documents to data/
└─→ Run notebook cells to verify indexing works

Step 3: Test the Streamlit UI
└─→ Run app.py in Colab with localtunnel
└─→ Verify chatbot interface works correctly

Step 4: Deploy to production
└─→ Push to GitHub
└─→ Deploy to Hugging Face Spaces
└─→ Embed in your website

Step 5: Publish website
└─→ Enable GitHub Pages
└─→ Share your live URL!
```

### Phase 3: When You're Ready for Production

Once you've tested everything in Colab and your chatbot works well:

1. ✅ Make sure all your documents are in the `data/` folder
2. ✅ Push your code to GitHub
3. ✅ Deploy to Hugging Face Spaces (see next section)
4. ✅ Embed the permanent Hugging Face URL in your website

---

## 💻 Option 2: Testing Locally on Your Computer

If you prefer to develop on your local machine, follow these steps.

### Prerequisites

- Python 3.9+ installed
- Terminal/Command Prompt access
- Text editor or IDE (VS Code recommended)

### Setup Steps

1. **Clone your repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. **Create a virtual environment**:
   
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

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**:
   ```bash
   # Copy the template
   cp .env.example .env
   
   # Edit .env and add the instructor-provided key
   # OPENAI_API_KEY=your-instructor-provided-key-here
   ```

5. **Add your documents** to the `data/` folder:
   ```bash
   # Place your PDF, HTML, TXT files in data/
   ls data/
   ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
   
   The app will open at `http://localhost:8501` 🎉

### Testing Locally

1. **First run**: The app will index your documents (takes 10-30 seconds)
2. **Subsequent runs**: Loads from cached `storage/` folder (much faster)
3. **To re-index**: Delete the `storage/` folder and restart

### Local Development Tips

✅ **Advantages**:
- Faster iteration (no need to reinstall packages each time)
- Persistent storage (index cache survives between sessions)
- Works offline (once dependencies are installed)
- Better debugging experience

⚠️ **Remember**:
- Keep your virtual environment activated when working
- Never commit `.env` file to GitHub
- Test thoroughly before deploying to Hugging Face

### Workflow for Local Development

```bash
# 1. Activate environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Make changes to your code or data/

# 3. Test locally
streamlit run app.py

# 4. When satisfied, push to GitHub
git add .
git commit -m "Update chatbot"
git push

# 5. Deploy to Hugging Face (see next section)
```

---

## 🎯 Which Option Should You Choose?

| Factor | Google Colab | Local Development |
|--------|--------------|-------------------|
| **Setup Time** | ⚡ Instant | 🕐 10-15 minutes |
| **No Installation** | ✅ Yes | ❌ Need Python |
| **Persistent Environment** | ❌ Sessions expire | ✅ Always available |
| **Speed** | 🐌 Slower | ⚡ Faster |
| **Best For** | Beginners, quick tests | Serious development |
| **Internet Required** | ✅ Always | ❌ Only for deployment |

**Recommendation**: Start with Google Colab to learn, then switch to local development if you want a better experience!

### Understanding the Workflow

```
📝 Colab Notebook → 🧪 Test RAG Logic → 🚀 Deploy to Hugging Face → 🌐 Embed in Website
```

- **Colab**: Development and testing environment
- **Hugging Face**: Production hosting for your Streamlit app
- **Website**: User-facing integration

---

## 🧪 Testing with the Example

### Option 1: Use the Example Notebook in Colab

1. Open `examples/llama_test.ipynb` in Google Colab
2. Run all cells to see the chatbot in action
3. Ask questions like:
   - "When did Taylor Swift become a superstar?"
   - "What are the amendments in the Constitution?"

### Option 2: Copy Example Data for Testing

If you want to test with the example documents:

1. Clone the example data to your Google Drive
2. Or download from GitHub and upload to Colab
3. Point your code to the example data folder

---

## 🌐 Deploying to Hugging Face

### Why Deploy?
- ✨ Makes your chatbot publicly accessible
- 🆓 Free hosting for public projects
- 🔗 Easy to share with your team and embed in websites
- 🎨 Professional Streamlit interface

### Deployment Steps

1. **Create a new Space** at [huggingface.co/new-space](https://huggingface.co/new-space)
   - Name: `your-company-chatbot`
   - License: Apache 2.0
   - SDK: **Streamlit** ⚠️ Important!
   - Hardware: CPU Basic (free)

2. **Upload your files** from your GitHub repository:
   - `app.py` ✅
   - `requirements.txt` ✅
   - `data/` folder with YOUR documents ✅
   - `storage/` folder (optional - speeds up first load) ⚠️

3. **Add your API key as a Secret**:
   - Go to Space Settings → Repository secrets
   - Add secret: `OPENAI_API_KEY` = `your-key-here`
   - ⚠️ This is required for the chatbot to work!

4. **Wait for build** (2-3 minutes)
   - Check the "Logs" tab for any errors
   - Look for: "✅ Index loaded" or "✅ Index created"
   - Once running, your chatbot is live! 🎉

Your chatbot URL will be: `https://huggingface.co/spaces/YOUR-USERNAME/your-company-chatbot`

### 💡 Pro Tips for Hugging Face Deployment
- Upload the `storage/` folder to skip indexing on first load (faster startup)
- Test thoroughly in Colab or locally before deploying
- Use descriptive Space names (e.g., `acme-support-bot` not `test123`)
- The chatbot uses `gpt-5-nano-2025-08-07` for responses and `text-embedding-3-small` for indexing (configured in app.py)

---

## 🌍 Embedding in Your Website

Once deployed to Hugging Face, you can embed your chatbot in your company website HTML page.

### Option 1: Floating Chat Widget (Recommended)

**See it in action**: Check out `visuals/embeddedui-demo.html` for a working example!

Add this code before the closing `</body>` tag of your `index.html`:

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
    background: white;
  }

  .chat-widget-container.open {
    display: block;
    animation: slideUp 0.3s ease;
  }

  @keyframes slideUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
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
    transition: all 0.3s ease;
  }

  .chat-widget-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  }

  @media (max-width: 768px) {
    .chat-widget-container {
      width: calc(100vw - 40px);
      height: calc(100vh - 140px);
      bottom: 10px;
      right: 10px;
    }
  }
</style>

<!-- Chatbot Toggle Button -->
<button class="chat-widget-button" onclick="toggleChat()" aria-label="Open chatbot">💬</button>

<!-- Chatbot Container -->
<div class="chat-widget-container" id="chatWidget">
  <iframe 
    src="https://huggingface.co/spaces/YOUR-USERNAME/your-company-chatbot"
    width="100%" 
    height="100%" 
    frameborder="0"
    title="Company Chatbot">
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
      button.setAttribute('aria-label', 'Open chatbot');
    } else {
      widget.classList.add('open');
      button.textContent = '✕';
      button.setAttribute('aria-label', 'Close chatbot');
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
  frameborder="0"
  title="Company Chatbot">
</iframe>
```

**⚠️ Important**: Replace `YOUR-USERNAME/your-company-chatbot` with your actual Space URL!

### Customization
- Change colors by editing the CSS `background` gradients
- Adjust size with `width` and `height` properties
- Move position with `bottom` and `right` values
- Customize the button emoji (💬, 🤖, 💡, etc.)

---

## 🚀 Publishing Your Website to GitHub Pages

Once you have your chatbot embedded, publish your complete website live on GitHub Pages!

### Step 1: Prepare Your Repository

Make sure your repository has:
- ✅ `index.html` (your main website page with embedded chatbot)
- ✅ `style.css` (your website styles)
- ✅ `app.py` (your chatbot code)
- ✅ `data/` folder (your company documents)
- ✅ `requirements.txt`
- ✅ `README.md`

### Step 2: Push Everything to GitHub

```bash
# Add all files
git add .

# Commit with a descriptive message
git commit -m "Add company website with AI chatbot"

# Push to your repository
git push origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for deployment

### Step 4: Access Your Live Website

Your website will be live at:
```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/
```

🎉 **Your chatbot is now embedded in a live website!**

### What Gets Published

- ✅ Your `index.html` website
- ✅ All CSS, JavaScript, and assets
- ✅ The embedded Hugging Face chatbot iframe
- ❌ Backend files (app.py, data/) are not served by GitHub Pages
- ℹ️ The chatbot itself runs on Hugging Face, not GitHub Pages

### Updating Your Live Site

Every time you push to GitHub, your site automatically updates:

```bash
# Make changes to your HTML/CSS
git add index.html style.css
git commit -m "Update website design"
git push origin main
# Site updates in 1-2 minutes!
```

### Pro Tips
- Test your website locally by opening `index.html` in a browser before pushing
- Make sure your Hugging Face Space URL in the iframe is correct
- Use relative paths for CSS/JS files (e.g., `./style.css` not `/style.css`)
- Add a custom domain in GitHub Pages settings if you have one!

---

## 🔧 Troubleshooting

### Google Colab Issues

#### "OPENAI_API_KEY not found"
- ✅ **Colab**: Make sure you added the secret (🔑 icon) and toggled "Notebook access" to ON
- ✅ **Local**: Check that your `.env` file exists and contains the instructor-provided key
- ✅ **Hugging Face**: Verify the secret is set in Settings → Repository secrets
- ✅ Make sure the key is exactly as provided by your instructor (no extra spaces)

#### "Runtime disconnected"
- ✅ Colab Pro (FREE for students!) has longer runtimes than the free tier
- ✅ Save your work frequently to GitHub or Google Drive
- ✅ Consider running critical tasks in shorter sessions

#### "Module not found" error
- ✅ Run the install cells at the start of your notebook
- ✅ Use `!pip install` (with !) in Colab, not regular `pip install`
- ✅ Make sure you ran the **entire** installation cell and waited for it to complete
- ✅ If issues persist, restart runtime (Runtime → Restart runtime) and run install cell again

### Chatbot Issues

#### "Please add documents to the 'data' directory"
- ✅ Make sure you uploaded files to the data folder
- ✅ Check that files are in supported formats (PDF, HTML, TXT, etc.)
- 💡 Try the example: upload files from `examples/data/`

#### Chatbot gives wrong answers
- ✅ Make sure your documents contain the relevant information
- ✅ Try rephrasing your question more specifically
- ✅ Check if the document text is readable (not corrupted or image-only PDFs)
- 💡 Test with the example first to verify it's working

#### Slow response times in Colab
- ⏱️ First query after starting is always slower (building index)
- ⚡ Subsequent queries should be faster (using cached index)
- 🚀 Get Colab Pro for FREE with your .edu email for better performance

### Hugging Face Deployment Issues

#### Space won't start
- ✅ Check the "Logs" tab for error messages
- ✅ Verify `OPENAI_API_KEY` is set in Repository secrets
- ✅ Make sure you selected "Streamlit" as the SDK
- ✅ Confirm you uploaded `requirements.txt` and `app.py`

#### Embedded iframe not showing chatbot
- ✅ Make sure your Hugging Face Space is running (check the Space URL directly)
- ✅ Try hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- ✅ Check browser console for errors (F12 → Console tab)
- ✅ Verify the iframe src URL is correct

### GitHub Pages Issues

#### Website not loading
- ✅ Make sure GitHub Pages is enabled in Settings → Pages
- ✅ Wait 1-2 minutes after enabling for initial deployment
- ✅ Check that branch is set to `main` and folder is `/ (root)`

#### Chatbot iframe not appearing on live site
- ✅ Verify your Hugging Face Space URL is correct in the iframe src
- ✅ Check browser console for CORS or iframe errors
- ✅ Test the Hugging Face Space URL directly in a browser first

#### CSS/JavaScript not loading
- ✅ Use relative paths: `./style.css` not `/style.css`
- ✅ Check file names match exactly (case-sensitive on GitHub Pages)
- ✅ Clear browser cache and hard refresh

---

## 📚 Additional Resources

- [Google Colab Documentation](https://colab.research.google.com/notebooks/welcome.ipynb)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)

---

## 📝 Project Integration (ENGCMP 0600)

This chatbot template is designed for your company project:

| Project Step | What to Do | Where |
|--------------|-----------|-------|
| **Steps 1-5** | Plan your company, identify documents needed | Team planning |
| **Step 6** | Research and gather company documents | `data/` folder |
| **Steps 7-9** | Test and refine your chatbot | Google Colab |
| **Step 8** | Deploy chatbot to production | Hugging Face Spaces |
| **Step 8** | Build website and embed chatbot | HTML/CSS with iframe |
| **Step 9** | Push repository and publish website | GitHub → GitHub Pages |
| **Step 10** | Present your live website with chatbot | Final demo |

### Deliverables Checklist
- ✅ Working chatbot with your company's documents
- ✅ Chatbot deployed to Hugging Face Spaces
- ✅ Company website with embedded chatbot
- ✅ **Website live on GitHub Pages**
- ✅ **Complete repository pushed to GitHub**
- ✅ Documentation (README, etc.)
- ✅ Google Colab notebook showing development process

---

## 🎓 Recommended Workflow

```
1. 📘 Learn RAG Concepts
   └─→ Open examples/llama_test.ipynb in Google Colab
   └─→ Understand how document indexing and retrieval works

2. 📝 Plan Your Company
   └─→ Identify what documents your chatbot needs
   └─→ Gather company information (products, policies, FAQs)

3. 📄 Prepare Documents
   └─→ Collect and organize documents in supported formats
   └─→ Add to data/ folder

4. 🧪 Choose Development Environment
   └─→ Option A: Google Colab (browser-based, beginner-friendly)
   └─→ Option B: Local development (faster, more control)

5. 🔧 Test Your Chatbot
   └─→ Google Colab: Use localtunnel for temporary testing
   └─→ Local: Run streamlit run app.py for instant feedback
   └─→ Verify answers are accurate and relevant

6. 🚀 Deploy to Production
   └─→ Push code to GitHub repository
   └─→ Deploy to Hugging Face Spaces (permanent hosting)
   └─→ Get your permanent chatbot URL

7. 🌐 Build Company Website
   └─→ Create index.html with company branding
   └─→ Embed Hugging Face chatbot using iframe code
   └─→ Style with CSS

8. 📤 Publish Website
   └─→ Push website files to GitHub
   └─→ Enable GitHub Pages in repository settings
   └─→ Get your live website URL

9. ✅ Verify Everything Works
   └─→ Test chatbot on live website
   └─→ Ask various questions to ensure accuracy
   └─→ Check responsive design on mobile

10. 🎤 Present Your Project
    └─→ Demo your live website with working AI chatbot
    └─→ Explain your company and how the bot helps customers
    └─→ Share both GitHub and live website URLs
```

---

## 🤝 Support

If you run into issues:
1. ✅ Check the [Troubleshooting](#troubleshooting) section above
2. 🧪 Try running the `examples/llama_test.ipynb` to verify setup
3. 📋 Review your code against this README
4. 🔍 Check Hugging Face Space logs for error messages
5. 💬 Ask your instructor or TA for help

---

## 🎓 Learning Resources

- **`examples/llama_test.ipynb`** - Jupyter notebook explaining RAG concepts (start here!)
- **`examples/README.md`** - How the example chatbot works
- **`data/README.md`** - Tips for adding documents
- **`visuals/`** - UI demos and screenshots for reference

---

**Good luck building your AI-powered chatbot! 🚀**

> Remember: Develop in Google Colab, deploy to Hugging Face, embed in your website, publish on GitHub Pages!