import os
import boto3

BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-v2")  # or another model

def generate_answer(question, contexts):
    context = "\n".join(contexts)
    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {question}
Answer:"""

    bedrock = boto3.client(
        "bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-1"),
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )

    response = bedrock.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body={"prompt": prompt, "max_tokens_to_sample": 300}
    )
    # The API format may differ depending on the model
    answer = response["body"]["completion"]
    return answer