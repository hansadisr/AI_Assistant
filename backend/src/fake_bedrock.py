import random
import numpy as np

def fake_get_embedding(text: str):
    """
    Pretends to convert text into a 1536-number embedding vector.
    Real Bedrock would return actual meaningful numbers.
    We use a TRICK: hash the text into a repeatable random seed,
    so the same text always gives the same fake embedding 
    (good enough for testing the pipeline mechanics).
    """
    seed = abs(hash(text)) % (10 ** 8)
    rng = np.random.default_rng(seed)
    return rng.random(1536).tolist()  # Titan embeddings are 1536 dimensions

def fake_generate_answer(query: str, context: str):
    """
    Pretends to be Claude answering a question.
    Just returns a clearly-labeled fake response so you can see
    the pipeline works end-to-end.
    """
    return (
        f"[FAKE RESPONSE - replace with real Bedrock tomorrow]\n\n"
        f"You asked: '{query}'\n"
        f"I found {len(context.split(chr(10)+chr(10)))} relevant chunks of context.\n"
        f"A real Claude response would summarize that context here."
    )