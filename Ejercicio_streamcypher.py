import random
from random import randint

# Keystream Aleatorio
def keystream_rand(size, seed):
    random.seed(seed)
    key = []
    for i in range(size):
        key.append(random.randint(0, 255))
    return bytes(key)
def encrypt(plaintext, keystream):
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append(plaintext[i] ^ keystream[i])
    return bytes(ciphertext)
def decrypt(ciphertext, keystream):
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ keystream[i])
    return bytes(plaintext)

texto = "Hola Mundo"
# Convertir el texto a binario
binario = texto.encode('utf-8')
# Generar un keystream aleatorio del mismo tamaño que el texto
seed = 12345
keystream = keystream_rand(len(binario), seed)
#keystream_bytes = bytes(keystream)
# Encriptar el texto
ciphertext = encrypt(binario, keystream)
print(f"Texto original: {texto}")
print(f"Texto en binario: {binario}")
print(f"Keystream: {keystream}")
print(f"Texto encriptado: {ciphertext}")
# Desencriptar el texto
decrypted_text = decrypt(ciphertext, keystream) 
print(f"Texto desencriptado: {decrypted_text.decode('utf-8')}")
