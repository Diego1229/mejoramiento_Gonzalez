""" Determinar los divisores de un número introducido por
teclado """
def divisores (num):
    for i in range(1,num+1): # inicia desde uno y a la variable num se le agrega uno
       if num% i== 0:
        print(i)

num=int(input("ingrese un numero positivo: "))
divisores(num + 1 )
