import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==============================
# Application
# ==============================

APP_NAME = "GenLogix AI"

APP_VERSION = "1.0"

APP_DESCRIPTION = """
An Autonomous Multi-Agent Generative AI Platform
for Transportation Bottleneck Analysis
and Logistics Cost Optimization
"""

# ==============================
# Gemini
# ==============================

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.3

# ==============================
# Embedding
# ==============================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ==============================
# FAISS
# ==============================

FAISS_PATH = "faiss_db"

# ==============================
# Upload
# ==============================

UPLOAD_FOLDER = "uploads"

# ==============================
# Chunking
# ==============================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 5