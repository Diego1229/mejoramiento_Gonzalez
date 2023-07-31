#Calcular el máximo de números positivos introducidos por
#teclado, sabiendo que metemos números hasta que
#introduzcamos uno negativo. El negativo no cuenta."""

def maximo_positivo():
    maximo=None #en la variable maximo se agregan los numeros positivos ingresados por el usuario y mantiene un valor maximo, no se asigna ningun valor por none, esto indica que aun no a encontrado ningun numero valido 

    while True:   # Bucle infinito, seguirá pidiendo números hasta que se ingrese uno negativo.
        try:
             numero=int(input("ingrese un numero positivo"))
        
             if numero < 0:
                 break      # Si el número ingresado es negativo, se rompe el bucle para terminar la entrada de números.
        
             if maximo is None or numero > maximo:  #is none (esto verifica si la variable es igual al none)
                 maximo = numero                    # Se actualiza maximo con el valor del número ingresado si es mayor.
                                                    #maximo siempre va acontener el numero mas largo
        except ValueError:
             print("error introducir un numero valido") # error al escribir un valor entero

    return maximo    #al que finaliza el bucle, se devuelve el valor maximo que se a encontrado  

resultado = maximo_positivo ()    # se llama la funcion y se guarda en la variable resultado                                        

if resultado is not None: # si el resultado es none, es para saber si se encontraron numeros positivos validos  
   
    print("el maximo de los numeros es:",resultado )

else:
    print("no se introdujo ningun numero positivo")    