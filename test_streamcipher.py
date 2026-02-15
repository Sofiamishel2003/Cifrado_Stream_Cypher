import unittest

from Ejercicio_streamcypher import encrypt, decrypt


class TestStreamCipherXOR(unittest.TestCase):

    def test_descifrado_recupera_mensaje_original(self):
        # Ejemplo 1
        m1 = "Por la mañana café"
        k1 = 39853
        c1 = encrypt(m1, k1)
        self.assertEqual(decrypt(c1, k1), m1)

        # Ejemplo 2
        m2 = "Por la tarde Ron"
        k2 = 898
        c2 = encrypt(m2, k2)
        self.assertEqual(decrypt(c2, k2), m2)

        # Ejemplo 3
        m3 = "Ya estamo en la calle, sal de tu balcón"
        k3 = 120
        c3 = encrypt(m3, k3)
        self.assertEqual(decrypt(c3, k3), m3)

    def test_diferentes_claves_producen_diferente_ciphertext(self):
        msg = "Por la mañana café"
        c_a = encrypt(msg, 39853)
        c_b = encrypt(msg, 39854)  # clave distinta
        self.assertNotEqual(c_a, c_b)

    def test_misma_clave_mismo_ciphertext_determinismo(self):
        msg = "Por la tarde Ron"
        key = 898
        c1 = encrypt(msg, key)
        c2 = encrypt(msg, key)
        self.assertEqual(c1, c2)

    def test_mensajes_diferentes_longitudes(self):
        # Corto
        corto = "Hi"
        key = 120
        c_corto = encrypt(corto, key)
        self.assertEqual(decrypt(c_corto, key), corto)

        # Mediano
        mediano = "Por la tarde Ron"
        c_med = encrypt(mediano, key)
        self.assertEqual(decrypt(c_med, key), mediano)

        # Largo 
        largo = "Ya estamo en la calle, sal de tu balcón"
        c_largo = encrypt(largo, key)
        self.assertEqual(decrypt(c_largo, key), largo)

        # Además valida que el tamaño del ciphertext coincide con el del plaintext en bytes
        self.assertEqual(len(c_corto), len(corto.encode("utf-8")))
        self.assertEqual(len(c_med), len(mediano.encode("utf-8")))
        self.assertEqual(len(c_largo), len(largo.encode("utf-8")))


if __name__ == "__main__":
    unittest.main()
