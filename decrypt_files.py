# import required module
from cryptography.fernet import Fernet
#opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()
file_name=str(input('Enter the name of the file:'))
# using the key
fernet = Fernet(key)
# opening the encrypted file
with open(file_name, 'rb') as enc_file:
	encrypted = enc_file.read()
# decrypting the file
decrypted = fernet.decrypt(encrypted)
# opening the file in write mode and
# writing the decrypted data
with open(file_name, 'wb') as dec_file:
	dec_file.write(decrypted)
