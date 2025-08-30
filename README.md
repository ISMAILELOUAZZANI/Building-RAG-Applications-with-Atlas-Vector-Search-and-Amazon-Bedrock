# Building RAG Applications with Atlas Vector Search and Amazon Bedrock

## Overview

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) application using:
- **MongoDB Atlas Vector Search** for semantic search and retrieval of relevant documents.
- **Amazon Bedrock** for advanced language model generation (e.g., Anthropic Claude, Amazon Titan, etc).

## Features

- Ingest and vectorize documents into MongoDB Atlas.
- Query Atlas Vector Search for relevant contexts.
- Use Amazon Bedrock to generate answers augmented with retrieved data.
- Simple REST API for querying the RAG pipeline.

---

## Architecture

```
User Query
    |
    v
[API Endpoint] ---> [Atlas Vector Search] ---> [Amazon Bedrock LLM]
    |                                         (Context Injection)
    v
Response
```

---

## Setup

### 1. Prerequisites

- Python 3.9+
- MongoDB Atlas account (with Vector Search enabled)
- AWS account (with access to Amazon Bedrock)
- `pip install -r requirements.txt`

---

### 2. Configuration

- Copy `.env.example` to `.env` and fill in your API keys and connection URIs.

---

### 3. Run the App

```bash
uvicorn app.main:app --reload
```

---

### 4. Example Usage

```bash
curl -X POST http://localhost:8000/ask \
    -H "Content-Type: application/json" \
    -d '{"question": "What is Atlas Vector Search?"}'
```
---

## File Structure

- `app/main.py` - FastAPI app and RAG pipeline logic
- `app/ingest.py` - Document ingestion and embedding
- `app/bedrock_client.py` - Amazon Bedrock client
- `app/vector_search.py` - Atlas Vector Search logic
- `requirements.txt` - Dependencies
- `.env.example` - Sample environment config

---

## License

MIT