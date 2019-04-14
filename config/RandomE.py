from cryptography.fernet import Fernet

class EncripDecrip():
    def __init__(self):
        self.key=Fernet.generate_key()
        self.code=Fernet(self.key)

    def encrip(self, text):
        texto=text.encode()
        enc_text=self.code.encrypt(texto)
        return enc_text

    def decrip(self, text):
        texto=text.encode()
        dec_text=self.code.decrypt(texto)
        return dec_text.decode()

    def encripfiles(self, file, output):
        with open(file, "rb") as f:
            data=f.read()
        data_encrypted=self.code.encrypt(data)

        with open(output, "wb") as f:
            f.write(data_encrypted)

    def decriptfiles(self, files, output):
        with open(files, "rb") as f:
            data=f.read()
        data_decrypted=self.code.decrypt(data)

        with open(output, "wb") as f:
            f.write(data_decrypted)