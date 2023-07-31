import random # Importar el módulo random para generar números aleatorios

def calcular_lista(): # Definir la función calcular_lista

    n = int(input("Ingrese el tamaño de la lista:"))

    lista = []  # creamos una lista vasia 
    for i in range(n):
        lista.append(random.randint(1, 100))
    print("La lista original es:", lista)  # Imprimir la lista original con los numeros aleatoreos que el usuario ingreso

    suma = sum(lista)
    print("La suma de la lista es:", suma) ## Calcular la suma de todos los elementos de la lista
    
    promedio = suma / n
    print("El promedio de la lista es:", promedio) # Calcular el promedio de los elementos de la lista
    
    mayor=max(lista)
    print("El numero mayor de la lista es", mayor) # Calcular el promedio de los elementos de la lista

    menor = min(lista)
    print("El número menor de la lista es:", menor)   # Calcular el promedio de los elementos de la lista

    ascendente = sorted(lista)
    print("Lista ordenada de manera ascendente:", ascendente)  # Calcular el promedio de los elementos de la lista

    descendente = sorted(lista, reverse=True)
    print("Lista ordenada de una forma descendente:", descendente) # Ordenar la lista de forma descendente y mostrarla

    numero = int(input("Ingrese el número que desea buscar en la lista:"))
    
    if numero in lista: # Ordenar la lista de forma descendente y mostrarla
        
        posicion = lista.index(numero)  #index buscamos un elemnto expecifico en la lista 
        print("El número", numero, "se encuentra en la posición", posicion, "de la lista.")
    else:
        # Si el número no está en la lista, mostrar un mensaje indicándolo
        print("El número", numero, "no se encuentra en la lista.")

calcular_lista() # Llamar a la función calcular_lista para que se ejecute

