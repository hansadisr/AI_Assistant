import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from rag_engine import ask

result = ask("What services does Moderta offer?")
print("Answer:", result["answer"])
print("Sources:", result["sources"])