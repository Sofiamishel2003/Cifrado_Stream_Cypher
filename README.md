
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

Aquí tienes la sección completa lista para copiar y pegar en tu README, incluyendo exactamente los ejemplos que mostraste.

---

# Parte 2 – Análisis de Seguridad

---

## 2.1 Variación de la Clave

Para demostrar el impacto de cambiar la clave, se utilizó el mismo texto pero con dos seeds distintas.

### Ejemplo práctico

```
=== STREAM CIPHER XOR (Demo) ===
1) Generar keystream (hex)
0) Salir
Elige una opción: 1
Texto (para tamaño del keystream): Hola ron con cola
Seed/clave (entero): 22
Keystream (hex): 477c0ce45e3db028768919a35bdc180a87
```

Luego, con el mismo texto pero distinta seed:

```
=== STREAM CIPHER XOR (Demo) ===
1) Generar keystream (hex)
0) Salir
Elige una opción: 1
Texto (para tamaño del keystream): Hola ron con cola
Seed/clave (entero): 333
Keystream (hex): b3b46ecf2a90aed6817ea97adb2fad1984
```

### ¿Qué sucede cuando cambia la clave utilizada para generar el keystream?
Aunque el mensaje fue exactamente el mismo, el keystream generado cambió completamente al modificar la seed. Esto pasa porque cuando se genera el keystream es en base a la seed, entonces se vuelve algo super diferente generado, después cómo se hace el XOR entre el texto plano y el keystream genera algo super diferente. Así refleja como un cambio en la clave hace que sea casi indecifrable con otra.

---

## 2.2 Reutilización del Keystream

Se cifraron dos mensajes distintos utilizando la misma seed.

### Ejemplo práctico

Primer mensaje:

```
=== STREAM CIPHER XOR (Demo) ===
Elige una opción: 2
Texto a cifrar: Ataque al amanecer
Seed/clave (entero): 999
Ciphertext (hex): 698f9632d754402deb3be0a615a343e96914
```

Segundo mensaje:

```
=== STREAM CIPHER XOR (Demo) ===
Elige una opción: 2
Texto a cifrar: Ataque al anochecer
Seed/clave (entero): 999
Ciphertext (hex): 698f9632d754402deb3be0a51bae4eef6f0318
```

### Observación importante

Los primeros bytes de ambos ciphertext son casi idénticos porque ambos mensajes comparten el mismo prefijo:

"Ataque al a..."

Esto ya revela información estructural del mensaje. Lo que propone que sea objetivo de fuerza bruta y se pueda encontrar algo, cómo con un análisis de frecuencia para decifrar frases o conjuntos simples y poder determinar a partir de ahí la clave utiizada. Esto significa que si el atacante conoce uno de los mensajes, puede recuperar el otro aplicando XOR nuevamente. Esta es una vulnerabilidad crítica en los cifrados de flujo cuando se reutiliza el keystream.

---

## 2.3 Longitud del Keystream
Si el keystream es más corto que el mensaje y se reutiliza o repite para cubrir todo el texto, se introduce un patrón periódico. Esto puede permitir ataques estadísticos y filtrado de información estructural del mensaje.

Usualmente en como se maneja y en mi implementación el keystream se genera con la misma longitud que el mensaje, lo que evita repeticiones dentro del mismo texto. Aunque, si se reutiliza la misma seed para varios mensajes, se vuelve a utilizar exactamente el mismo keystream completo, generando la vulnerabilidad descrita en el inciso 2.2.

---

## 2.4 Consideraciones Prácticas

En un entorno de producción real, se deben considerar varios aspectos críticos:

1. No reutilizar el keystream: Cada mensaje debe utilizar un nonce o vector de inicialización único junto con la clave secreta.

2. Protección de la clave: La seed no debe estar hardcodeada ni expuesta en el código fuente. Debe manejarse mediante mecanismos seguros de almacenamiento.

3. Manejo seguro entre receptor y emisor: la manera en que se compartan las claves entre ellos para poder leer y envíar mensajes entre ambos debe de ser muy segura para no exponer cómo se cifran los datos y poder tener una comunicación segura.
