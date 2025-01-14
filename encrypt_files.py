# import required module
from cryptography.fernet import Fernet
# key generation
key = Fernet.generate_key()
  
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)
file_name=str(input('Enter the name of the file:'))
# opening the original file to encrypt
with open(file_name, 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open(file_name, 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
