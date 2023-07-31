import random

def comparar_lista():

    lista1=[] # Inicializamos dos listas vacías para almacenar los números generados
    lista2=[]

    n=int(input("ingrese el tamaño de la lista1:")) # El usuario ingresa el tamaño de ambas listas
    y=int(input("ingrese el tamaño de la lista2:"))
  
    for i in range(n):
      lista1.append(random.randint(1, 100))  # Generamos números aleatorios y los agregamos a lista1
    print("La lista1 original es:", lista1)
    
    for i in range(y):
     lista2.append(random.randint(1, 100))   # Generamos números aleatorios y los agregamos a lista2
    print("La lista2 original es:", lista2)
    
    suma_lista1 = sum(lista1)  # Calculamos la suma de ambas listas
    suma_lista2 = sum(lista2)

    print("La suma de la lista 1 es:", suma_lista1)
    print("La suma de la lista 2 es:", suma_lista2)

    if suma_lista1 > suma_lista2: # Comparamos las sumas y mostramos un mensaje indicando cuál lista tiene la suma mayor, o si ambas sumas son iguales.
      print("La suma de la lista 1 es mayor que el de la lista 2.")

    elif suma_lista2 > suma_lista1:
      print("La suma de la lista 2 en mayor que el de la lista 1.")
    
    else:
      print("La suma de las dos listas son iguales.")


def determinar_mayor_menor(lista1, lista2):
    
    menor_lista1=min(lista1)  # Utilizamos la función min() para encontrar el número menor en lista1 y lo imprimimos
    print("El numero menor de la lista1 es:", menor_lista1)

    menor_lista2=min(lista2)
    print("El numero menor de la lista2 es:", menor_lista2)

# Llamamos a la función comparar_lista() para ejecutar el programa y realizar las comparaciones entre las listas generadas aleatoriamente.
comparar_lista()