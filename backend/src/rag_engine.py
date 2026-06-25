import json
import numpy as np
import faiss
import pickle
import sys, os

sys.path.append(os.path.dirname(__file__))
from config import FAISS_INDEX_PATH, CHUNKS_PATH, USE_FAKE_BEDROCK

if USE_FAKE_BEDROCK:
    from fake_bedrock import fake_get_embedding as get_embedding
    from fake_bedrock import fake_generate_answer as generate_answer_raw
else:
    from bedrock_client import get_embedding, generate_answer_raw

# Load the knowledge base once when this module is imported
index = faiss.read_index(FAISS_INDEX_PATH)
with open(CHUNKS_PATH, "rb") as f:
    chunks = pickle.load(f)

def retrieve(query: str, top_k: int = 3):
    query_embedding = np.array([get_embedding(query)], dtype="float32")
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]

def ask(query: str):
    relevant_chunks = retrieve(query)
    context = "\n\n".join([c["text"] for c in relevant_chunks])
    answer = generate_answer_raw(query, context)
    sources = list(set(c["source"] for c in relevant_chunks))
    return {"answer": answer, "sources": sources}