import json
import numpy as np
import faiss
import pickle
import sys, os
from langchain_text_splitters import RecursiveCharacterTextSplitter

sys.path.append(os.path.dirname(__file__))
from config import RAW_DATA_PATH, FAISS_INDEX_PATH, CHUNKS_PATH, USE_FAKE_BEDROCK

if USE_FAKE_BEDROCK:
    from fake_bedrock import fake_get_embedding as get_embedding
else:
    from bedrock_client import get_embedding  # we'll build this tomorrow

if __name__ == "__main__":
    # Load scraped content
    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        documents = json.load(f)

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = []
    for doc in documents:
        splits = splitter.split_text(doc["content"])
        for chunk in splits:
            chunks.append({"text": chunk, "source": doc["url"]})

    print(f"Created {len(chunks)} chunks")

    # Generate embeddings (fake or real, depending on config)
    print("Generating embeddings...")
    embeddings = []
    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk["text"])
        embeddings.append(emb)
        if i % 10 == 0:
            print(f"  {i}/{len(chunks)} done")

    embeddings_array = np.array(embeddings, dtype="float32")

    # Build FAISS index
    dimension = embeddings_array.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)

    # Save
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print(f"\n✅ Knowledge base built! {index.ntotal} vectors saved.")