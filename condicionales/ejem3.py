# hacer un programa que pida 3 numeros y determinar cual es mayor
valido = False

while not valido:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))

        if num1 >= num2 and num1 >= num3:
            print(f"El número mayor es {num1}")
            valido = True
        elif num2 >= num1 and num2 >= num3:
            print(f"El número mayor es {num2}")
            valido = True
        elif num3 >= num1 and num3 >= num2:
            print(f"El número mayor es {num3}")
            valido = True
        else:
            print("Ingrese números válidos. Intente nuevamente.")
    except ValueError:
        print("Ingrese números válidos. Intente nuevamente.")

print("¡Gracias por utilizar el programa!")
