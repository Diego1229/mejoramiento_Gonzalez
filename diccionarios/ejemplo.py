#hacer un diccionario de 10 colores en español y ingles con el bucle for 
def crea_diccionario():
    diccionario={"rojo": "red",
            "blanco": "white",
            "verde": "green", 
            "negro": "black",
            "rosado": "pink",
            "amarillo": "yellow",
            "naranja": "orange",
            "purpura": "purple",
            "azul": "blue",
            "lila": "lilac",}

colores= ['rojo','blanco','verde','negro','rosado','amarillo', 'naranja', 'purpura', 'azul', 'lila', 'marron']
diccionario= crea_diccionario
# Recorremos la lista de colores y verificamos si cada color está en el diccionario.
# Si está en el diccionario, mostramos la traducción al inglés.
# Si no está en el diccionario, mostramos un mensaje indicando que no está presente.
for colores in colores:
    if colores in diccionario:
        print(colores, "->", diccionario[colores])
    else:
        print(colores, "no esta en el diccionario")

#modificar el nombre 
diccionario["rojo"]='morado'
print(diccionario)
