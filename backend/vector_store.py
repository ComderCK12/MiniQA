import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def load_documents(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    elif ext in [".doc", ".docx"]:
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    return loader.load()


def create_vectorstore_from_file(uploaded_file):
    file_path = f"uploaded_docs/{uploaded_file.name}"

    # Save uploaded file
    os.makedirs("uploaded_docs", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Load and split
    documents = load_documents(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    # Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore