"""Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa"""

def cuenta_cifras(numero):
    
    if numero ==0: # Si el número es igual a 0, tiene una sola cifra, así que retornamos 1
        return 1
   
    contador=0 #inicializamos la variable en 0 para contar las cifras  
    
    while numero >0: # mientras que el numero sea mayor que =
        numero//=10   # se divide el numero por 10
        contador += 1 # se incrementa en contador en 1
    
    return contador #retorna total de lascifras 

try:
    numero=int(input("ingrese un numero entre 0 y 9,999: "))
    
    if 0 <= numero <= 9999: # verificamos si el numero ingresado esta dentro del rango permitido
        
        y= cuenta_cifras(numero) # se llama ala funcion para obtener la cantidad de cifras del numero
        
        print(f"El número {numero} tiene {y} cifra(s).")
    else:
        print("Error: El número debe estar entre 0 y 9,999.")

except ValueError:
    print("Error: Por favor, ingrese solo números válidos.")
