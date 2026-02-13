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

def menu():
    while True:
        print("\n=== STREAM CIPHER XOR (Demo) ===")
        print("1) Generar keystream (hex)")
        print("2) Cifrar texto")
        print("3) Descifrar ciphertext (desde hex)")
        print("4) Demo rápida (Hola Mundo)")
        print("0) Salir")

        op = input("Elige una opción: ").strip()

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            texto = input("Texto (para tamaño del keystream): ")
            seed = int(input("Seed/clave (entero): "))
            data = texto.encode("utf-8")
            ks = keystream_rand(len(data), seed)
            print("Keystream (hex):", ks.hex())
            print("Keystream (bytes):", ks)

        elif op == "2":
            texto = input("Texto a cifrar: ")
            seed = int(input("Seed/clave (entero): "))
            ct = encrypt(texto, seed)
            print("Ciphertext (hex):", ct.hex())
            print("Ciphertext (bytes):", ct)

        elif op == "3":
            hex_ct = input("Ciphertext en hex (ej: 0a1b...): ").strip()
            seed = int(input("Seed/clave (entero): "))
            try:
                ct = bytes.fromhex(hex_ct)
            except ValueError:
                print("Hex inválido. Asegúrate de pegar solo caracteres 0-9 y a-f.")
                continue

            try:
                pt = decrypt(ct, seed)
                print("Texto descifrado:", pt)
            except UnicodeDecodeError:
                print("No se pudo decodificar como UTF-8. (¿seed incorrecto o dato no era texto?)")

        elif op == "4":
            texto = "Hola Mundo"
            seed = 12345
            ct = encrypt(texto, seed)
            pt = decrypt(ct, seed)
            ks = keystream_rand(len(texto.encode("utf-8")), seed)
            print("Texto:", texto)
            print("Seed:", seed)
            print("Keystream (hex):", ks.hex())
            print("Ciphertext (hex):", ct.hex())
            print("Descifrado:", pt)

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()