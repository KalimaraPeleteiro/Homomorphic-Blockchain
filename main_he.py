from src.homomorphic_blockchain import HomomorphicBlockchain 
from src.blockchain_metrics import BlockchainMetrics

def run_blockchain_tests():
    configs = [
        {'difficulty': 2, 'num_blocks': 5, 'transactions_per_block': 5},
        {'difficulty': 2, 'num_blocks': 10, 'transactions_per_block': 10},
        {'difficulty': 2, 'num_blocks': 10, 'transactions_per_block': 20},
        {'difficulty': 2, 'num_blocks': 20, 'transactions_per_block': 10},
        {'difficulty': 2, 'num_blocks': 20, 'transactions_per_block': 20},

        {'difficulty': 3, 'num_blocks': 5, 'transactions_per_block': 5},
        {'difficulty': 3, 'num_blocks': 10, 'transactions_per_block': 10},
        {'difficulty': 3, 'num_blocks': 10, 'transactions_per_block': 20},
        {'difficulty': 3, 'num_blocks': 20, 'transactions_per_block': 10},
        {'difficulty': 3, 'num_blocks': 20, 'transactions_per_block': 20},
    ]

    for i, config in enumerate(configs):
        print(f"\nTestando Blockchain. Teste Nº{i + 1} com {config['num_blocks']} blocos e dificuldade {config['difficulty']}...")
        
        blockchain = HomomorphicBlockchain(difficulty=config['difficulty'])
        for i in range(10):
            blockchain.create_wallet(initial_balance=10000000)

        blockchain_metrics = BlockchainMetrics(blockchain)
        total_block_size = 0

        # Create multiple blocks with transactions
        for _ in range(config['num_blocks']):
            blockchain.create_multiple_blocks(1, config['transactions_per_block'])

            # Record metrics after block creation
            block, hashes_attempted, mining_time = blockchain.create_block()
            blockchain_metrics.record_block_creation(hashes_attempted, mining_time)

            total_block_size += block.get_size_in_bytes()

        # Collect and print metrics for the blockchain
        metrics = blockchain_metrics.get_metrics()

        total_transactions = config['num_blocks'] * config['transactions_per_block']
        total_time = metrics['total_time']
        
        tps = total_transactions / total_time if total_time > 0 else 0
        avg_block_size = total_block_size / config['num_blocks'] if config['num_blocks'] > 0 else 0

        print(f"Metrics for Blockchain Test {i + 1}:")
        print(f"  Total Blocks: {metrics['total_blocks']}")
        print(f"  Total Transactions: {total_transactions}")
        print(f"  Transactions per Block: {config['transactions_per_block']}")
        print(f"  Avg Block Creation Time: {metrics['avg_block_creation_time']:.4f} seconds")
        print(f"  Avg Hashes per Block: {metrics['avg_hashes_per_block']}")
        print(f"  Avg Mining Time: {metrics['avg_mining_time']:.4f} seconds")
        print(f"  Total Time: {total_time:.4f} seconds")
        print(f"  Transactions per Second (TPS): {tps:.4f} transactions.")
        print(f"  Average Block Size: {avg_block_size:.4f} bytes")

if __name__ == "__main__":
    run_blockchain_tests()
