import time
from src.block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0') # Bloco Gênese

    def create_block(self, data = "", previous_hash=""):
        if previous_hash == "":
            previous_hash = self.chain[-1].hash if self.chain else '0'
        index = len(self.chain) + 1 
        timestamp = time.time()
        hash = Block.calculate_hash(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(block)
        return block