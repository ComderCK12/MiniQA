import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "chroma_store")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")