from src.blockchain import Blockchain
from random import randint

if __name__ == "__main__":
    blockchain = Blockchain()

    for i in range(100):
        blockchain.create_block(data=f"{randint(1, 10000)}")
    
    for block in blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Hash: {block.hash}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Data: {block.data}")
        print(f"  Timestamp: {block.timestamp}\n")