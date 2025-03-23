import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

load_dotenv()

MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")

class MongoDBUtil:
    def __init__(self, database_name: str):
        """
        Initializes MongoDB connection.
        :param database_name: Name of the database
        """
        self.client : MongoClient = MongoClient(MONGODB_CONNECTION_STRING)
        self.database: Database = self.client[database_name]
    
    def get_collection(self, collection_name: str) -> Collection:
        """Gets a collection by name."""
        return self.database[collection_name]
    
    def insert_one(self, collection_name: str, document: Dict[str, Any]) -> Any:
        """Inserts a single document into the collection."""
        collection = self.get_collection(collection_name)
        return collection.insert_one(document).inserted_id
    
    def insert_many(self, collection_name: str, documents: List[Dict[str, Any]]) -> List[Any]:
        """Inserts multiple documents into the collection."""
        collection = self.get_collection(collection_name)
        return collection.insert_many(documents).inserted_ids
    
    def find_one(self, collection_name: str, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Finds a single document matching the query."""
        collection = self.get_collection(collection_name)
        return collection.find_one(query)
    
    def find_many(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Finds multiple documents matching the query."""
        collection = self.get_collection(collection_name)
        return list(collection.find(query))
    
    def update_one(self, collection_name: str, query: Dict[str, Any], update_values: Dict[str, Any]) -> Any:
        """Updates a single document matching the query."""
        collection = self.get_collection(collection_name)
        return collection.update_one(query, {"$set": update_values}).modified_count
    
    def update_many(self, collection_name: str, query: Dict[str, Any], update_values: Dict[str, Any]) -> int:
        """Updates multiple documents matching the query."""
        collection = self.get_collection(collection_name)
        return collection.update_many(query, {"$set": update_values}).modified_count
    
    def delete_one(self, collection_name: str, query: Dict[str, Any]) -> int:
        """Deletes a single document matching the query."""
        collection = self.get_collection(collection_name)
        return collection.delete_one(query).deleted_count
    
    def delete_many(self, collection_name: str, query: Dict[str, Any]) -> int:
        """Deletes multiple documents matching the query."""
        collection = self.get_collection(collection_name)
        return collection.delete_many(query).deleted_count
    
    def count_documents(self, collection_name: str, query: Dict[str, Any]) -> int:
        """Counts the number of documents matching the query."""
        collection = self.get_collection(collection_name)
        return collection.count_documents(query)
    
    def create_index(self, collection_name: str, keys: List[str], unique: bool = False) -> str:
        """Creates an index on the specified fields."""
        collection = self.get_collection(collection_name)
        index_keys = [(key, 1) for key in keys]
        return collection.create_index(index_keys, unique=unique)
    
    def close_connection(self):
        """Closes the MongoDB connection."""
        self.client.close()
