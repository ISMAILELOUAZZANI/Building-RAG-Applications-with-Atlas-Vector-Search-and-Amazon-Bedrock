import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.vector_search import find_relevant_docs
from app.bedrock_client import generate_answer

class QueryRequest(BaseModel):
    question: str

app = FastAPI()

@app.post("/ask")
def ask_question(request: QueryRequest):
    # Step 1: Retrieve relevant documents from Atlas
    contexts = find_relevant_docs(request.question)
    # Step 2: Generate answer from Bedrock LLM
    answer = generate_answer(request.question, contexts)
    return {"answer": answer, "contexts": contexts}