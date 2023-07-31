#medir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos       
def num_medio( x, y, z):
    
    menor = min( x, y, z) # Encuentra el menor número entre x, y y z
    mayor = max( x , y, z)

    
    medio = x + y + z - menor - mayor # Calcula el número medio

    return medio  

try:
    
    x = int(input("Ingrese el primer número: "))   # se solicita al usuario los tres numeros
    y = int(input("Ingrese el segundo número: "))
    z = int(input("Ingrese el tercer número: "))


    
    medio = num_medio(x, y, z) #se llama la funcion para calcular el numero medio
    

    print(f"El número medio es: {medio}") # se imprime el numero medio calculado 
    
except ValueError:
    print("Error: Por favor, ingrese solo números válidos.")