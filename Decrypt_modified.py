from cryptography.fernet import Fernet as F
def load_key():
    return open('Key.key','rb').read()
key=load_key()
f=F(key)
message=str(input('Enter the message you want to decrypt:-')).encode()
decrypted=f.decrypt(message)
print(decrypted)
