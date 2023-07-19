# construir un programa que, al recibir como dato N numeros naturales, determine
#cunato de ellos son positivos, negativos o nulos 

#si el usuario escribe un numero incorrecto, el programa no se ejecuta.
#se debe preguntar denuevo por la informacion hasta que el dato ingresado sea correcto.
comprobar = True
while comprobar == True:

   N = int(input("ingrese la cantidad de datos que se desea procesar: "))


   if N > 0:
        comprobar= 0
        positivo= 0
        negativo= 0
        nulos=0
    
        for i in range (N):
            dato= int(input("ingrese el numero natural: "))
    
            if dato > 0:
                positivo += 1

            elif dato < 0: 
                negativo += 1  

            else:
                 nulos += 1     

        print("La cantidad de numeros positivos fue", positivo,
             "\nLa cantidad de numeros negarivos fue",negativo,
             "\nLa cantidad de numeros nulos fueron",nulos )            

   else:
    print("El numero que ha ingresado no es correcto. Intentelo nuevamente.")