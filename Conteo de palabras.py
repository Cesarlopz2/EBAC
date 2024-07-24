from collections import defaultdict

# Ingresar el texto con el que se trabajará
texto = "El amor es una locura que ni el cura lo cura porque si el cura lo cura sería una locura del cura"

# Separar el texto en palabras para poder realizar el conteo
palabras = texto.split()

# Crear un diccionario para almacenar los conteos
conteo_palabras = defaultdict(int)

# Definir algunas condiciones para cada palabra
for palabra in palabras:
    # Eliminar signos de puntuación al final de la palabra para un conteo preciso
    palabra = palabra.strip(".,;:!?'")
    # Convertir la palabra a minúsculas 
    palabra = palabra.lower() 
    # Realizar el conteo de las palabras    
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Imprimir el número de veces que cada palabra se repite
for palabra, conteo in conteo_palabras.items():
    print(f"'{palabra}' se repite {conteo} veces.")

