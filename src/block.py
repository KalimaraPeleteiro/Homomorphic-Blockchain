import hashlib
import time


class Block:

    def __init__(self, index, previous_hash, timestamp, data, hash) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
    
    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(value.encode()).hexdigest()
    
    