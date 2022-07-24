from cryptography.fernet import Fernet


class Crypto:
    def __init__(self, key):
        self.fernet = Fernet(key)
        self.key = key

    def encrypt(self, data):
        return self.fernet.encrypt(data)

    def decrypt(self, data):
        return self.fernet.decrypt(data)

    def match_key(self, key):
        return self.key == key