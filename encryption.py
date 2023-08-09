from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encryptor():

    def createKey(self):
        key = Fernet.generate_key()
        return key
    
    def writeKey(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def loadKey(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
            return key
        
    def encryptString(self, key, password):
        password = password.encode()
        f = Fernet(key)
        encrypted_password = f.encrypt(password)
        return encrypted_password
    
    def decryptString(self, key, encrypted_password):
        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password)
        return decrypted_password
    
test = Encryptor()
mykey = test.createKey()
test.writeKey(mykey, 'test.key')
loaded_key = test.loadKey('test.key')
password = test.encryptString(loaded_key, 'test')
test.decryptString(loaded_key, password)