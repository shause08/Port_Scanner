from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import shutil

key = RSA.generate(2048)

with open('private_key.pem', 'wb') as private_key_file:
    private_key_file.write(key.export_key())

public_key = key.publickey()

with open('public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_key.export_key())

script_directory = os.path.dirname(os.path.abspath(__file__))

source_directory = os.path.join(script_directory, 'source')

destination_directory = os.path.join(script_directory, 'destination')

shutil.copytree(source_directory, destination_directory)

file_list = os.listdir(destination_directory)

for file_name in file_list:
    file_path = os.path.join(destination_directory, file_name)
    
    with open(file_path, 'rb') as file:
        data = file.read()
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(data)
    
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

sub_dir = 'destination'

for file_name in file_list:
    encrypted_file_path = os.path.join(script_directory, sub_dir, file_name + '.encrypted')

    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        cipher = PKCS1_OAEP.new(key)
        decrypted_data = cipher.decrypt(encrypted_data)

    decrypted_file_path = os.path.join(script_directory, sub_dir, file_name + '_dechiffre.txt')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
