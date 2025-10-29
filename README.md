# 🚀 MiniQA: Intelligent Document Question Answering App

MiniQA is a lightweight, intelligent document-based Q\&A application that leverages the power of **Streamlit, LangChain, and Google Gemini** to provide precise, context-aware answers from your documents.

-----

## ✨ Key Features

  * **Document Processing:** Effortlessly upload and process your own documents for analysis.
  * **Instant Q\&A:** Ask natural language questions and receive instant, AI-generated answers based solely on the document content.
  * **Powered by Gemini:** Uses **Google Gemini** for state-of-the-art natural language understanding and generation.
  * **RAG Architecture:** Built with **LangChain** for robust Retrieval-Augmented Generation (RAG).
  * **Seamless UI:** Simple and interactive interface powered by **Streamlit**.

-----

## 💻 Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend/UI** | Streamlit | Simple and fast web application development. |
| **Backend** | Python, LangChain | Core logic, data orchestration, and chaining. |
| **Embeddings & LLM** | Google Gemini (via `langchain-google-genai`) | Generative model and embedding services. |
| **Vector Store** | FAISS | Efficient in-memory storage for document embeddings. |
| **Environment** | Conda / Virtualenv | Dependency and environment management. |

-----

## 🛠️ Installation Steps

### 1\. Clone the Repository

```bash
git clone https://github.com/yourusername/MiniQA.git
cd MiniQA
```

### 2\. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

**Using Conda:**

```bash
conda create -n miniqa python=3.10
conda activate miniqa
```

**Or using venv:**

```bash
python -m venv miniqa
source miniqa/bin/activate   # Use miniqa\Scripts\activate on Windows
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

-----

## 🔑 Environment Setup

You **must** create a file named `.env` in the root `MiniQA/` directory. This file stores your API key and configuration settings.

### Example `.env` file:

```ini
GOOGLE_API_KEY=your_gemini_api_key_here
CHROMA_DB_DIR=chroma_store
```

> ⚠️ **Security Note:** Never share your API key publicly or commit the `.env` file to version control systems like GitHub.

-----

## ▶️ Run the Application

Once installation and environment setup are complete, start the application:

```bash
streamlit run app.py
```

Open your browser and navigate to: **[http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)**

-----

## 📂 Folder Structure

```
MiniQA/
├── app.py                       # Main Streamlit application file
├── backend/
│   ├── qa_chain.py              # Logic for creating the Q&A chain
│   └── vector_store.py          # Logic for document processing and embedding
├── requirements.txt             # List of Python dependencies
├── .env                         # Environment variables (API Key)
└── README.md                    # Project documentation
```

-----

## 💡 Future Enhancements

  * Add support for multiple document uploads.
  * Include chat history and context retention for conversational Q\&A.
  * Integrate with other LLM providers (e.g., OpenAI or Anthropic Claude).

-----

### Author

**Chirag Kathoye**
IT Analyst @ NPCI
🔗 **LinkedIn:** [https://linkedin.com/in/chiragkathoye](https://linkedin.com/in/chiragkathoye)

> **Quote:** “Ask smarter questions, get smarter answers — with MiniQA 💬”