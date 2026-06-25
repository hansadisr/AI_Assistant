import os

# Get the project's root folder (one level up from src/)
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(SRC_DIR)

RAW_DATA_PATH = os.path.join(BACKEND_DIR, "data", "raw", "moderta_content.json")
FAISS_INDEX_PATH = os.path.join(BACKEND_DIR, "data", "processed", "moderta_index.faiss")
CHUNKS_PATH = os.path.join(BACKEND_DIR, "data", "processed", "moderta_chunks.pkl")

AWS_REGION = "us-east-1"  # update once you know your company's region
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v1"
GENERATION_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

# Toggle this to True once you have real AWS credentials
USE_FAKE_BEDROCK = True