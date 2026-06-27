import os

# Get the project's root folder (one level up from src/)
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(SRC_DIR)

RAW_DATA_PATH = os.path.join(BACKEND_DIR, "data", "raw", "moderta_content.json")
FAISS_INDEX_PATH = os.path.join(BACKEND_DIR, "data", "processed", "moderta_index.faiss")
CHUNKS_PATH = os.path.join(BACKEND_DIR, "data", "processed", "moderta_chunks.pkl")

AWS_REGION = "eu-north-1"
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
GENERATION_MODEL_ID = "amazon.nova-lite-v1:0"

USE_FAKE_BEDROCK = False