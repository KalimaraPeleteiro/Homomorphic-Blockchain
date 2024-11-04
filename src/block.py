import hashlib


class Block:
    """
    Classe que representa um bloco na blockchain.
    """

    def __init__(self, index, previous_hash, timestamp, transactions, hash, nonce) -> None:
        """
        Inicializa um novo bloco.

        :param index: O índice do bloco na cadeia.
        :param previous_hash: O hash do bloco anterior.
        :param timestamp: O timestamp de criação do bloco.
        :param transactions: A lista de transações contidas no bloco.
        :param hash: O hash do bloco.
        :param nonce: O número usado para encontrar o hash válido.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash
        self.nonce = nonce


    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, transactions, nonce):
        """
        Calcula o hash para um bloco.

        :param index: O índice do bloco.
        :param previous_hash: O hash do bloco anterior.
        :param timestamp: O timestamp de criação do bloco.
        :param transactions: As transações no bloco.
        :param nonce: O número utilizado para a mineração.
        :return: O hash calculado do bloco.
        """
        value = f"{index}{previous_hash}{timestamp}{transactions}{nonce}"
        return hashlib.sha256(value.encode()).hexdigest()
