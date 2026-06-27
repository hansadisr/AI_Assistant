# test_embedding.py
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="eu-north-1")

response = client.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({"inputText": "Hello, this is a test sentence."})
)

result = json.loads(response["body"].read())
print("Embedding length:", len(result["embedding"]))
print("First 5 values:", result["embedding"][:5])