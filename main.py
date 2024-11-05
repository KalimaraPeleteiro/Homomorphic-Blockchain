from src.blockchain import Blockchain
from src.blockchain_metrics import BlockchainMetrics

def run_blockchain_tests():
    configs = [
        {'difficulty': 2, 'num_blocks': 5, 'transactions_per_block': 5},
        {'difficulty': 4, 'num_blocks': 10, 'transactions_per_block': 10},
        {'difficulty': 6, 'num_blocks': 20, 'transactions_per_block': 20},
    ]

    for i, config in enumerate(configs):
        print(f"\nRunning Blockchain Test {i + 1} with difficulty {config['difficulty']}...")
        
        blockchain = Blockchain(difficulty=config['difficulty'])
        for i in range(10):
            blockchain.create_wallet(initial_balance=10000000)

        blockchain_metrics = BlockchainMetrics(blockchain)

        # Create multiple blocks with transactions
        for _ in range(config['num_blocks']):
            blockchain.create_multiple_blocks(1, config['transactions_per_block'])

            # Record metrics after block creation
            block, hashes_attempted, mining_time = blockchain.create_block()
            blockchain_metrics.record_block_creation(hashes_attempted, mining_time)

        # Collect and print metrics for the blockchain
        metrics = blockchain_metrics.get_metrics()
        print(f"Metrics for Blockchain Test {i + 1}:")
        print(f"  Total Blocks: {metrics['total_blocks']}")
        print(f"  Total Transactions: {metrics['total_transactions']}")
        print(f"  Avg Transactions per Block: {metrics['avg_tx_per_block']}")
        print(f"  Avg Block Creation Time: {metrics['avg_block_creation_time']:.4f} seconds")
        print(f"  Avg Hashes per Block: {metrics['avg_hashes_per_block']}")
        print(f"  Avg Mining Time: {metrics['avg_mining_time']:.4f} seconds")
        print(f"  Total Time: {metrics['total_time']:.4f} seconds")

if __name__ == "__main__":
    run_blockchain_tests()
