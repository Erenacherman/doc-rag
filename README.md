# 📚 DocChat — PDF Question Answering with RAG

DocChat is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the contents of a PDF.

Instead of sending the entire PDF directly to an LLM, DocChat:

1. Extracts text from the PDF
2. Splits the text into smaller chunks
3. Converts chunks into embeddings
4. Stores the embeddings in ChromaDB
5. Retrieves the most relevant chunks for a question
6. Builds a context-aware prompt
7. Sends the context and question to a cloud LLM
8. Returns an answer based on the provided document

The current version uses **OpenRouter** as the cloud LLM provider.

---

## ✨ Features

- 📄 PDF document processing
- ✂️ Text chunking
- 🧠 Sentence-transformer embeddings
- 🗄️ ChromaDB vector database
- 🔎 Similarity-based document retrieval
- 🤖 RAG-based question answering
- ☁️ OpenRouter cloud LLM support
- 📚 Displays retrieved document sources/pages
- 🔐 API keys are loaded from environment variables
- 💻 Can run locally without requiring a local LLM

---

## 🏗️ Project Architecture

```text
PDF
 │
 ▼
Document Loader
 │
 ▼
Text Splitter
 │
 ▼
Text Chunks
 │
 ▼
Embedding Model
 │
 ▼
ChromaDB
 │
 ▼
Similarity Search
 │
 ▼
Relevant Chunks
 │
 ▼
Context Builder
 │
 ▼
RAG Prompt
 │
 ▼
OpenRouter Cloud LLM
 │
 ▼
Answer
```

---

## 📁 Project Structure

```text
docchat/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   └── uploads/
│       └── .gitkeep
│
├── vectorstore/
│   └── chroma/
│
├── src/
│   ├── ingestion/
│   │   ├── loader.py
│   │   └── splitter.py
│   │
│   ├── embeddings/
│   │   └── embedder.py
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── rag/
│   │   ├── context.py
│   │   └── prompt.py
│   │
│   └── llm/
│       ├── cloud_llm.py
│       └── llm_factory.py
│
└── tests/
```

> The exact files may change as the project evolves.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd docchat
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your GitHub repository.

---

## 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If you are developing the project and dependencies are not yet listed in `requirements.txt`, install the packages used by the project and then generate the file:

```bash
pip freeze > requirements.txt
```

---

# 🔐 Configure OpenRouter

DocChat uses an API key to access the cloud LLM.

## 1. Create your environment file

Copy the example:

```bash
cp .env.example .env
```

## 2. Open `.env`

```bash
nano .env
```

Add your own configuration:

```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

Replace:

```text
YOUR_OPENROUTER_API_KEY
```

with your own API key.

### ⚠️ Important

Never commit `.env` to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
vectorstore/
```

The `.env.example` file is safe to commit because it should contain only placeholder values.

---

# 📄 Add a PDF

Place the PDF you want to chat with inside:

```text
data/uploads/
```

For the current console version, the application expects:

```text
data/uploads/test.pdf
```

Example:

```text
data/
└── uploads/
    └── test.pdf
```

---

# ▶️ Run the Application

Activate your virtual environment first:

```bash
source venv/bin/activate
```

Then:

```bash
python app.py
```

The application will process the PDF and eventually display:

```text
Ask a question (type 'exit' to stop):
```

Example:

```text
Ask a question (type 'exit' to stop): What is supervised learning?
```

Type:

```text
exit
```

to stop the application.

---

# 🔎 How RAG Works in DocChat

Suppose the PDF contains information about machine learning.

When the user asks:

```text
What is supervised learning?
```

DocChat does not simply send the question to the LLM.

Instead:

### Step 1 — Convert the PDF into text

```text
PDF → Documents
```

### Step 2 — Split the document

```text
Documents → Chunks
```

### Step 3 — Create embeddings

Each chunk is converted into a numerical vector:

```text
Text → Embedding Vector
```

### Step 4 — Store vectors

The vectors are stored in ChromaDB:

```text
Chunks + Embeddings → ChromaDB
```

### Step 5 — Search

The user's question is also converted into an embedding.

ChromaDB searches for the most similar chunks.

```text
Question
   ↓
Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
```

### Step 6 — Build context

The retrieved chunks are combined into context.

### Step 7 — Generate answer

The question and retrieved context are sent to the cloud LLM.

```text
Context + Question
       ↓
   OpenRouter
       ↓
     Answer
```

This is the core idea of **Retrieval-Augmented Generation (RAG)**.

---

# 🧩 Main Components

## Document Loader

Located at:

```text
src/ingestion/loader.py
```

Responsible for reading PDF files and extracting their contents.

---

## Text Splitter

Located at:

```text
src/ingestion/splitter.py
```

Breaks large documents into smaller chunks suitable for embedding and retrieval.

---

## Embedding Manager

Located at:

```text
src/embeddings/embedder.py
```

Converts text chunks into numerical vector representations.

---

## ChromaDB

Located at:

```text
src/vectorstore/chroma_store.py
```

Stores embeddings and provides similarity search.

---

## Retriever

Located at:

```text
src/retrieval/retriever.py
```

Finds the most relevant chunks from ChromaDB for a user's question.

---

## Context Builder

Located at:

```text
src/rag/context.py
```

Formats retrieved documents into context that can be given to the LLM.

---

## RAG Prompt

Located at:

```text
src/rag/prompt.py
```

Contains the instructions telling the LLM to answer using the retrieved document context.

---

## Cloud LLM

Located at:

```text
src/llm/cloud_llm.py
```

Handles communication with the cloud LLM provider through OpenRouter.

---

## LLM Factory

Located at:

```text
src/llm/llm_factory.py
```

Controls which LLM provider the application uses.

Currently:

```text
LLM_PROVIDER=openrouter
```

selects the OpenRouter cloud provider.

---

# 🛡️ Security

Never put API keys directly into Python source code.

❌ Do not do this:

```python
api_key = "my-secret-api-key"
```

✅ Use environment variables:

```python
import os

api_key = os.getenv("OPENROUTER_API_KEY")
```

And store the actual key in:

```text
.env
```

The `.env` file should never be committed to GitHub.

---

# 🧪 Testing

Tests are located inside:

```text
tests/
```

Run a test file with:

```bash
python tests/test_loader.py
```

Depending on the current project version, additional tests can be added for:

- PDF loading
- Text splitting
- Embeddings
- ChromaDB
- Retrieval
- RAG responses
- LLM integration

---

# ⚠️ Current Limitations

The current version is intentionally a basic RAG implementation.

Current limitations include:

- The console application currently expects a PDF at a configured path.
- PDF processing can take time for large documents.
- Vector embeddings take time on the first run.
- ChromaDB persistence and duplicate-document handling are still being improved.
- The application currently uses a cloud LLM through OpenRouter.
- Advanced retrieval techniques are not yet implemented.
- There is currently no production authentication or user management.
- The UI is currently console-based.

These are planned areas for future development.

---

# 🔮 Future Improvements

Possible future versions can include:

- 🌐 Streamlit web interface
- 📤 Drag-and-drop PDF upload
- 📚 Multiple PDF support
- ♻️ Duplicate PDF detection
- 🗑️ Delete indexed documents
- 💬 Chat history
- 📌 Source/page citations
- 🔎 Improved retrieval
- 🎯 Re-ranking
- ⚡ Faster document processing
- 📊 Retrieval evaluation
- 🧠 Multiple embedding models
- ☁️ Multiple LLM providers
- 🐳 Docker deployment
- 🚀 Cloud deployment

---

# 🎯 Project Goal

DocChat is designed as a practical learning project for understanding how modern RAG applications are built.

The project demonstrates the complete pipeline:

```text
Document Processing
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector Database
        ↓
Similarity Search
        ↓
Context Retrieval
        ↓
Prompt Construction
        ↓
LLM Generation
```

---

# 📜 License

This project is intended for educational and portfolio purposes.
