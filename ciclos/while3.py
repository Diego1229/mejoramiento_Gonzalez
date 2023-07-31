""". Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod. """

def obtener_cociente_reciduo(numero1, numero2):
    if numero1 >= numero2:    #se verifica cual de los dos numeros es mayor 
        mayor = numero1       #utilizando el if - else 
        menor =numero2
    else:
        mayor = numero2 
        menor = numero1
    
    cociente= 0 # se inicializa la variable  

    while mayor >= menor: # se utiliza el bucle while para restar el numero menor al numero mayor se repite hasta que el numero mayor sea menor que el numero menor
        mayor -= menor 
        cociente += 1
    
    return cociente, mayor #se retorna el cociente y el residuo como resultado de la función.

numero1= int(input("ingresar el primer numero"))
numero2= int(input("ingrese el segundo numero "))

cociente, residuo = obtener_cociente_reciduo(numero1, numero2) # sellama la funcion, con los valores ingresados por el usuario
                                                               #los valores cociente residuo, que se retornaron en la funcion se asignaron alas variables cociente y residuo       

print("El cociente de", numero1, "entre", numero2, "es:", cociente)
print("El residuo de", numero1, "entre", numero2, "es:", residuo)
