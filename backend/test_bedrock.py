import boto3
import json

# Create the Bedrock Runtime client
client = boto3.client(
    "bedrock-runtime",
    region_name="eu-north-1"
)

# Invoke Amazon Nova Lite
response = client.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    body=json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": "Hi, Nova."
                    }
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 100,
            "temperature": 0.7
        }
    })
)

# Read the response
result = json.loads(response["body"].read())

# Print the generated text
print(result["output"]["message"]["content"][0]["text"])