import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from rag_engine import ask

test_questions = [
    "What services does Moderta offer?",
    "Does Moderta have any job openings?",
    "What is the capital of France?",  # ← should say "I don't know" - out of scope!
]

for q in test_questions:
    print(f"\n{'='*60}")
    print(f"Q: {q}")
    result = ask(q)
    print(f"A: {result['answer']}")
    print(f"Sources: {result['sources']}")