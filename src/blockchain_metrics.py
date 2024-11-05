import time

class BlockchainMetrics:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.start_time = time.time()
        self.total_blocks = 0
        self.total_transactions = 0
        self.total_hashes = 0  
        self.total_time = 0
        self.total_mining_time = 0 


    def record_block_creation(self, hashes_attempted, mining_time):
        """
        Registra a criação de um novo bloco, atualizando os contadores de blocos e transações.
        Também coleta dados sobre o poder computacional usado para minerar o bloco.
        """
        self.total_blocks += 1
        self.total_transactions += len(self.blockchain.current_transactions)
        self.total_hashes += hashes_attempted
        self.total_mining_time += mining_time
        self.total_time = time.time() - self.start_time


    def get_metrics(self):
        """
        Retorna as métricas de desempenho.
        """
        avg_tx_per_block = self.total_transactions / self.total_blocks if self.total_blocks > 0 else 0
        avg_block_creation_time = self.total_time / self.total_blocks if self.total_blocks > 0 else 0
        avg_hashes_per_block = self.total_hashes / self.total_blocks if self.total_blocks > 0 else 0
        avg_mining_time = self.total_mining_time / self.total_blocks if self.total_blocks > 0 else 0

        return {
            'total_blocks': self.total_blocks,
            'total_transactions': self.total_transactions,
            'avg_tx_per_block': avg_tx_per_block,
            'avg_block_creation_time': avg_block_creation_time,
            'total_time': self.total_time,
            'avg_hashes_per_block': avg_hashes_per_block,
            'avg_mining_time': avg_mining_time
        }
