from src.blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.create_block(data="First block data")
    blockchain.create_block(data="Second block data")
    
    for block in blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Hash: {block.hash}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Data: {block.data}")
        print(f"  Timestamp: {block.timestamp}\n")