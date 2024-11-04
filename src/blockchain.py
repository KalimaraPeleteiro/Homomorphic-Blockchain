import time
import hashlib

from src.block import Block
from src.transaction import Transaction


class Blockchain:
    """
    Classe que representa a blockchain.
    """

    def __init__(self, difficulty=4):
        """
        Inicializa uma nova blockchain.

        :param difficulty: O nível de dificuldade para a mineração (número de zeros no hash).
        """
        self.chain = []
        self.difficulty = difficulty
        self.current_transactions = []        # Lista de Transações que serão validadas no bloco.
        self.create_block(previous_hash='0')  # Bloco Gênese


    def create_block(self, data="", previous_hash=""):
        """
        Cria um novo bloco e o adiciona à cadeia.

        :param data: Os dados a serem armazenados no bloco.
        :param previous_hash: O hash do bloco anterior.
        :return: O novo bloco criado.
        """

        # Verificando se é o Bloco Gênese
        if previous_hash == "":
            previous_hash = self.chain[-1].hash if self.chain else '0'

        # Extraindo os Para o Bloco
        index = len(self.chain) + 1
        timestamp = time.time()
        nonce = 0

        # Gerando PoW
        hash = self.proof_of_work(index, previous_hash, timestamp, self.current_transactions, nonce)

        # Criando Bloco e Adicionando a Rede
        block = Block(index, previous_hash, timestamp, self.current_transactions, hash, nonce)
        self.chain.append(block)

        self.current_transactions = [] # Resetando Transações
    
        return block
    

    def add_transaction(self, sender, recipient, amount):
        """
        Adiciona uma nova transação à lista de transações pendentes.

        :param sender: O endereço do remetente.
        :param recipient: O endereço do destinatário.
        :param amount: O valor da transação.
        """
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
    

    def proof_of_work(self, index, previous_hash, timestamp, transactions, nonce):
        """
        Realiza o processo de proof of work para encontrar um hash válido.

        O mecanismo de proof of work funciona tentando várias combinações de nonce até que
        o hash gerado comece com um número especificado de zeros (definido pela dificuldade).
        Isso é feito incrementando o nonce e recalculando o hash até que a condição seja satisfeita.

        :param index: O índice do bloco.
        :param previous_hash: O hash do bloco anterior.
        :param timestamp: O timestamp de criação do bloco.
        :param data: Os dados do bloco.
        :param nonce: O número utilizado para a mineração.
        :return: O hash que atende à condição de dificuldade.
        """
        hash = self.calculate_hash(index, previous_hash, timestamp, transactions, nonce)
        target = '0' * self.difficulty
        while not hash.startswith(target):
            nonce += 1
            hash = self.calculate_hash(index, previous_hash, timestamp, transactions, nonce)
        return hash


    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, transactions, nonce):
        """
        Calcula o hash para um bloco.

        :param index: O índice do bloco.
        :param previous_hash: O hash do bloco anterior.
        :param timestamp: O timestamp de criação do bloco.
        :param data: Os dados do bloco.
        :param nonce: O número utilizado para a mineração.
        :return: O hash calculado do bloco.
        """
        value = f"{index}{previous_hash}{timestamp}{transactions}{nonce}"
        return hashlib.sha256(value.encode()).hexdigest()
