import json
import random
from functools import lru_cache

from .mongodb_utils import MongoDBUtil  # type: ignore


def get_all_documents(collection_name):
    return _get_all_documents_cached(collection_name)

@lru_cache(maxsize=128)
def _get_all_documents_cached(collection_name):
    # Get all documents with their spawn probabilities
    db_util = MongoDBUtil()
    try:
        collection = db_util.get_collection(collection_name)
        all_items = list(collection.find({}, {"name": 1, "spawn_prob": 1, "_id": 1}))
        return all_items
    except Exception as e:
        print("Error in _get_all_documents_cached ", e)
    finally:
        db_util.close_connection()

def spawn_items(max_items=10):
    """
    Randomly selects items from a MongoDB collection based on each document's spawn_prob.
    
    Parameters:
    - max_items: Max number of items to spawn (default: 10)
    
    Returns:
    - List of spawned items
    """
    all_items = get_all_documents("items")
        
    if not all_items:
        return []
    
    # Create result list to store spawned items
    spawned_items = []
    
    # Perform independent probability checks for each slot
    for _ in range(max_items):
        # For each slot, evaluate all items independently based on their spawn probabilities
        candidates = []
        
        for item in all_items:
            # Get the spawn probability for this item
            spawn_prob = item.get("spawn_prob", 0)
            
            # Random check based on the item's probability
            if random.random() < spawn_prob:
                candidates.append(item)
        
        # If any items passed the probability check, randomly choose one
        if candidates:
            spawned_item = random.choice(candidates)
            spawned_items.append(spawned_item)
        
    return spawned_items