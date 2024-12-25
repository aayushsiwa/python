from cryptography.fernet import Fernet as F
def write_key():
    key=F.generate_key()
    with open('Key.key','wb') as key_file:
        key_file.write(key)
def load_key():
    return open('Key.key','rb').read()
write_key()
key=load_key()
f=F(key)
message=str(input('Enter the message you want to encrypt:-')).encode()
encrypted=f.encrypt(message)
print(encrypted)
