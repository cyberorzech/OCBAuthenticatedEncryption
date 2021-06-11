from Crypto.Cipher import AES
from Crypto import Random


import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), "utf-8")
unpad = lambda s: s[0 : -ord(s[-1:])]


class AESCipher:
    def __init__(self, key):
        self.key = bytes(key, "utf-8")

    def encrypt(self, raw):
        raw = pad(raw)
        iv = "encryptionIntVec".encode("utf-8")
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        iv = "encryptionIntVec".encode("utf-8")
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc)).decode("utf8")


# def encryptDataAES128(data):
#     key = Random.get_random_bytes(16)
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext = cipher.encrypt(data)
#     return ciphertext, key

# def decryptDataAES128(ciphertext, key):
#     cipher = AES.new(key, AES.MODE_CBC)
#     data = cipher.decrypt(ciphertext)
#     return data


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
