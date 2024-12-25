from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open('key.txt','wb') as key_file:
        key_file.write(key)
def load_key():
    return open('key.key','rb').read()
write_key()
key=load_key()
f=Fernet(key)
message='Some message'.encode()
encrypted=f.encrypt(message)
print(encrypted)
decrypted_encrypted=f.decrypt(encrypted)
print(decrypted_encrypted)
