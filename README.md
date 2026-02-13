
# Cifrado Stream Cipher XOR

## 📌 Descripción del Proyecto

Este laboratorio implementa un **Stream Cipher básico** utilizando la operación XOR y un generador pseudoaleatorio (`random`) como fuente de keystream.

El sistema:

* Genera un **keystream determinístico** a partir de una seed.
* Cifra un mensaje aplicando XOR byte a byte.
* Descifra el mensaje regenerando el mismo keystream.
* Incluye un menú interactivo para pruebas manuales.

El objetivo es comprender el rol del keystream en cifrados de flujo y analizar sus vulnerabilidades cuando se reutiliza.

---

## ⚙️ Requisitos

* Python 3.10 o superior
* No requiere librerías externas

---

## ▶️ Cómo Ejecutarlo

1. Abrir PowerShell o CMD.
2. Navegar al directorio del proyecto:

```powershell
cd "C:\Users\50250\Desktop\Sofía Mishell Velásquez UVG\Quinto año\Primer Semestre\Cifrado\Cifrado_Stream_Cypher"
```

3. Ejecutar el programa:

```powershell
python Ejercicio_streamcypher.py
```

O directamente:

```powershell
C:/Users/50250/AppData/Local/Microsoft/WindowsApps/python3.10.exe "Ejercicio_streamcypher.py"
```

---

## 📋 Menú Interactivo

Al ejecutar el programa aparece:

```
=== STREAM CIPHER XOR (Demo) ===
1) Generar keystream (hex)
2) Cifrar texto
3) Descifrar ciphertext (desde hex)
4) Demo rápida (Hola Mundo)
0) Salir
```

---

# 🧪 Ejemplos de Funcionamiento

---

## 🔹 Ejemplo 1 – Generación de Keystream

Entrada:

```
Texto: Hola Hermsoa Preciosa Bella Y Muchas Palabras de Afirmación
Seed: 323
```

Salida:

```
Keystream (hex):
39459d1be3a1a4eed6b469f91083b920d48d3a4de60b2457d8d0624c348a2bc4e860c6b7b94165fbf753e16e826bccb741050587b13aa32ae2f8adbc
```

Esto demuestra que el keystream depende completamente de la seed.

---

## 🔹 Ejemplo 2 – Cifrado

Texto plano:

```
Hola, soy yo y quiero mis palabras de afirmación porfavor
```

Seed utilizada:

```
323
```

Ciphertext generado:

```
712af17acf81d781af94109630fa9951a1e45f3f892b493eabf0122d58eb49b68913e6d3dc61049d9e218c0fe1020f042f2575e8c35cc25c8d8a
```

---

## 🔹 Ejemplo 3 – Descifrado

Ciphertext ingresado:

```
712af17acf81d781af94109630fa9951a1e45f3f892b493eabf0122d58eb49b68913e6d3dc61049d9e218c0fe1020f042f2575e8c35cc25c8d8a
```

Seed:

```
323
```

Resultado:

```
Hola, soy yo y quiero mis palabras de afirmación porfavor
```

✔ Se recupera exactamente el mensaje original.

---

## 🔹 Ejemplo 4 – Demo Rápida

Texto:

```
Hola Mundo
```

Seed:

```
12345
```

Keystream:

```
d50598bc638adf52bf3f
```

Ciphertext:

```
9d6af4dd43c7aa3cdb50
```

Descifrado:

```
Hola Mundo
```

---

# 🔐 Funcionamiento Técnico

El cifrado se basa en:

```
Ciphertext = Plaintext XOR Keystream
```

Y el descifrado en:

```
Plaintext = Ciphertext XOR Keystream
```

La propiedad fundamental utilizada es:

```
A XOR B XOR B = A
```

Por eso el mismo keystream debe regenerarse usando la misma seed.

---
