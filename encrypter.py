# -*- coding: utf-8 -*-

import os
import pyaes

# Abrir o arquivo para ser criptografado
file_name = 'texto.txt'
with open(file_name, 'rb') as file: 
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Definir chave
key = b'exemplochave1234'  # A chave deve ter 16 bytes para AES-128
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = file_name + '.crypto'
with open(new_file_name, 'wb') as new_file:  # `with` para segurança
    new_file.write(crypto_data)

print(f"Arquivo {file_name} foi criptografado para {new_file_name}")

