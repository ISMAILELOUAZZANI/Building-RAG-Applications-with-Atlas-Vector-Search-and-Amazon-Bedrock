import os
import json
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.environ["MONGODB_DB"]
COLLECTION_NAME = os.environ["MONGODB_COLLECTION"]
ATLAS_VECTOR_FIELD = os.environ.get("ATLAS_VECTOR_FIELD", "embedding")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def ingest_documents(docs):
    for doc in docs:
        embedding = embedder.encode([doc["text"]])[0].tolist()
        record = {
            "text": doc["text"],
            ATLAS_VECTOR_FIELD: embedding
        }
        collection.insert_one(record)

if __name__ == "__main__":
    # Example: load docs from a local JSON
    with open("data/docs.json") as f:
        docs = json.load(f)
    ingest_documents(docs)