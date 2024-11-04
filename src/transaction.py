import time

class Transaction:
    """
    Classe que representa uma transação na blockchain.
    """

    def __init__(self, sender, recipient, amount, timestamp=None):
        """
        Inicializa uma nova transação.

        :param sender: O endereço do remetente da transação.
        :param recipient: O endereço do destinatário da transação.
        :param amount: O valor da transação.
        :param timestamp: O timestamp da transação (opcional).
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp or time.time()
