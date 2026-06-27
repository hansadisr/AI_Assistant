import boto3
import json
from config import AWS_REGION, EMBEDDING_MODEL_ID, GENERATION_MODEL_ID

client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

def get_embedding(text: str):
    """Convert text into a vector embedding using Titan Embed v2."""
    response = client.invoke_model(
        modelId=EMBEDDING_MODEL_ID,
        body=json.dumps({"inputText": text})
    )
    result = json.loads(response["body"].read())
    return result["embedding"]

def generate_answer_raw(query: str, context: str):
    """Generate an answer using Amazon Nova Lite, grounded in retrieved context."""
    prompt = f"""You are a helpful assistant for Moderta, a sustainability consulting company.
Answer the question based ONLY on the context below. If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {query}

Answer:"""

    response = client.invoke_model(
        modelId=GENERATION_MODEL_ID,
        body=json.dumps({
            "messages": [
                {"role": "user", "content": [{"text": prompt}]}
            ],
            "inferenceConfig": {
                "maxTokens": 500,
                "temperature": 0.3
            }
        })
    )
    result = json.loads(response["body"].read())
    return result["output"]["message"]["content"][0]["text"]