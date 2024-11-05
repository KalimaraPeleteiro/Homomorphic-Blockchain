import time
from phe import paillier

class HomomorphicTransaction:
    """
    Classe que representa uma transação homomorficamente criptografada na blockchain usando o esquema Paillier.
    """

    def __init__(self, sender, recipient, amount, public_key, timestamp=None):
        """
        Inicializa uma nova transação homomorficamente criptografada.

        :param sender: O endereço do remetente da transação.
        :param recipient: O endereço do destinatário da transação.
        :param amount: O valor da transação.
        :param public_key: A chave pública Paillier para criptografar o valor.
        :param timestamp: O timestamp da transação (opcional).
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = self.encrypt_amount(amount, public_key)
        self.timestamp = timestamp or time.time()

    def encrypt_amount(self, amount, public_key):
        """
        Criptografa o valor da transação usando a chave pública Paillier.

        :param amount: O valor da transação.
        :param public_key: A chave pública Paillier.
        :return: O valor criptografado da transação.
        """
        return public_key.encrypt(amount)

    def decrypt_amount(self, private_key):
        """
        Descriptografa o valor da transação usando a chave privada Paillier.

        :param private_key: A chave privada Paillier.
        :return: O valor descriptografado da transação.
        """
        return private_key.decrypt(self.amount)

    def is_valid(self, wallets, private_key):
        """
        Valida a transação verificando se o remetente tem saldo suficiente.

        :param wallets: O dicionário de carteiras com saldos.
        :param private_key: A chave privada Paillier para descriptografar os saldos.
        :return: True se a transação for válida, False caso contrário.
        """
        if self.sender not in wallets:
            print(f"Sender {self.sender} not found.")
            return False
        
        # Descriptografando o saldo do remetente
        decrypted_balance = private_key.decrypt(wallets[self.sender]['balance'])
        
        # Descriptografando o valor da transação
        decrypted_amount = self.decrypt_amount(private_key)

        if decrypted_balance >= decrypted_amount:
            return True
        else:
            print(f"Fundos Insuficiente: Sender {self.sender} possui {decrypted_balance}, mas precisa {decrypted_amount}.")
            return False

    def to_dict(self):
        """
        Converte a transação para um dicionário serializável.

        :return: Um dicionário representando a transação.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': str(self.amount),  # Armazenar valor criptografado
            'timestamp': self.timestamp
        }
