import os
import pyaes

## abrir o arquivo criptografado

file_name = 'texto.txt.crypto'
file = open(file_name, "rb")
file_data = file.read()
file.close

## chave

key = b'exemplochave1234'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover arquivo criptografado

os.remove(file_name)

# criar arquivo descriptografado 

new_file = 'texto.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()


