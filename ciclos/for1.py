"""Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este """
    
def NumPerfecto(numero):   
    
    suma=0                 # se crea una variable para almacenar la suma de los divisores propios del numero 
    for i in range(1, numero):  # se utiliza para generar una secuencia de numeros que se utiliza como valores de i en el bucle, para verificar los divisores propios

        if (numero % i ==0):  # se realiza una division entre (numero) e (i), si al dividirlos no da ningun reciduo es numero perfecto
            suma+=i

    if numero == suma: #si es igual el numero es perfecto
        return True
    else:
        return False
        
try:  
    numero= int(input("introduzca un numero: ")) # se llama la funcion numPerfecto con el numero ingresado

    perfecto=NumPerfecto(numero)
    if perfecto ==True:
        print("es un numero perfecto")
    else:
        print("no es un numero perfecto") 

except ValueError:
    print("el caracter ingresado no es un numero ")
    print("vuelva a intentarlo")