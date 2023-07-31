#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos

def numero_medio(num1, num2, num3):
    
    menor = min(num1, num2, num3) # # Encontrar el número menor y mayor entre los tres números
    mayor = max(num1, num2, num3)

    # Calculamos el número medio utilizando operadores de comparación
    medio = num1 + num2 + num3 - menor - mayor

    return medio # Retornar el número medio calculado

try:
    # Pedimos al usuario que ingrese tres números   
    num1 = int(input("Ingrese el primer número: "))     
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    
    if num1!=num2!=num3:               # Verificar si los tres números son iguales
        print("Los tres numeros son iguales")

    # Llamamos a la función para encontrar el número medio
    medio = numero_medio(num1, num2, num3)
    
    print(f"El número medio es: {medio}")
    
    if num1!=num2!=num3: # # Verificar nuevamente si los tres números son iguales y mostrar un mensaje apropiado
        print("Los tres numeros son iguales")
    else:
        print("No es posible hallar el numero medio. ")
    
except ValueError: # Manejar una excepción si el usuario ingresa valores no numéricos
    print("Error: Por favor, ingrese solo números válidos.")
    