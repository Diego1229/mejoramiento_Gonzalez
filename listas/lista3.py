import random

def es_primo(numero):   # se define la funcion que verifica si un numero dado es primo o no retorna true si esprimo y false si no
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_posiciones(numero_buscado, arreglo): # esta funcion busca las posiciones donde aparecen numeros especificos en arreglos y las devuelve en una lista 
    posiciones = []
    for i in range(len(arreglo)):
        if arreglo[i] == numero_buscado:
            posiciones.append(i)
    return posiciones

def main(): # main seera la funcion principal del programa 
    
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    arreglo = [random.randint(1, 100) for _ in range(n)]

    primos = [num for num in arreglo if es_primo(num)]  #Se filtran los números primos del arreglo utilizando una comprensión de listas y se almacenan en la lista primos

    print("Arreglo:", arreglo) # se imprime el arreglo original
    print("Números primos en el arreglo:", primos)

    numero_buscado = int(input("Ingrese el número a buscar: "))
    veces_encontrado = arreglo.count(numero_buscado)  # se cuanta las veces que aprece el numero registrado por el usuario, busca en el arreglo y se almacena en la variable 
    posiciones = contar_posiciones(numero_buscado, arreglo) #Se llaman a la función contar_posiciones() para obtener las posiciones donde se encuentra el número buscado en el arreglo y se almacenan en la lista posiciones.

    print(f"El número {numero_buscado} aparece {veces_encontrado} veces en el arreglo.") #Finalmente, se imprime el número buscado, cuántas veces aparece y las posiciones donde se encuentra.
    print(f"Se encuentra en las posiciones: {posiciones}")                 

if __name__ == "__main__": #se utiliza para cuando se ejecute el codigo se ejecute directamente, pero no cuando se importe el archivo commo modulo 
    main()                  
