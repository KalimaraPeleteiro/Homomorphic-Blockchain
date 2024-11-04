from src.blockchain import Blockchain
from random import randint

if __name__ == "__main__":
    blockchain = Blockchain()

    for i in range(10):
        for j in range (10):
            blockchain.add_transaction(sender=f"address_{randint(1, 100)}", recipient=f"address_{randint(1, 100)}", amount=randint(1, 1000))
        blockchain.create_block(data=f"{randint(1, 10000)}")
    
    for block in blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Hash: {block.hash}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Transactions: {[(tx.sender, tx.recipient, tx.amount) for tx in block.transactions]}")
        print(f"  Timestamp: {block.timestamp}\n")