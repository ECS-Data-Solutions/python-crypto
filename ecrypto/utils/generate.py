from cryptography.fernet import Fernet


def generate_keys():
    return Fernet.generate_key()

print(generate_keys())
