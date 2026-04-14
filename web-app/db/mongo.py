from pymongo import MongoClient
from flask import current_app


_client = None


def get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(current_app.config["MONGO_URI"])
    return _client


def get_db():
    client = get_client()
    return client[current_app.config["MONGO_DB_NAME"]]


def get_predictions_collection():
    db = get_db()
    return db[current_app.config["MONGO_COLLECTION"]]