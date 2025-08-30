import os
import openai
from pymongo import MongoClient
import numpy as np

from sentence_transformers import SentenceTransformer

MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.environ["MONGODB_DB"]
COLLECTION_NAME = os.environ["MONGODB_COLLECTION"]
ATLAS_VECTOR_FIELD = os.environ.get("ATLAS_VECTOR_FIELD", "embedding")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Load your embedding model (same as used in ingest.py)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def find_relevant_docs(query, limit=3):
    query_embedding = embedder.encode([query])[0].tolist()
    pipeline = [
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": ATLAS_VECTOR_FIELD,
                "numCandidates": 100,
                "limit": limit,
                "index": "default"
            }
        }
    ]
    results = list(collection.aggregate(pipeline))
    # Return text chunks
    return [doc["text"] for doc in results]