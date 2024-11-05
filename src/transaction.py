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
    

    def is_valid(self, wallets):
        """
        Valida a transação verificando se o remetente tem saldo suficiente.
        
        :param wallets: O dicionário de carteiras com saldos.
        :return: True se a transação for válida, False caso contrário.
        """
        if self.sender not in wallets:
            print(f"Sender {self.sender} not found.")
            return False
        
        sender_balance = wallets[self.sender]
        if sender_balance >= self.amount:
            return True
        else:
            print(f"Fundos Insuficiente: Sender {self.sender} possui {sender_balance}, mas precisa {self.amount}.")
            return False
    

    def to_dict(self):
        """
        Converte a transação para um dicionário serializável.

        :return: Um dicionário representando a transação.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
