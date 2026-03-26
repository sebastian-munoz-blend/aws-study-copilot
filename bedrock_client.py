import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def get_bedrock_client():
    session = boto3.Session(
        profile_name=os.getenv("AWS_PROFILE"),
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )
    return session.client("bedrock-runtime")

def generate_response(messages, system_prompt):
    client = get_bedrock_client()
    model_id = os.getenv("MODEL_ID")

    response = client.converse(
        modelId=model_id,
        system=[{"text": system_prompt}],
        messages=messages,
        inferenceConfig={
            "maxTokens": 700,
            "temperature": 0.3,
            "topP": 0.9
        }
    )

    return response["output"]["message"]
