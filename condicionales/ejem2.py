#Hacer un programa que pida 2 numeros y se de cuenta cal de ellos es par, o si ambos lo son

numero1 = int(input("ingrese un numero:"))
numero2 =int(input("ingrese el segundo numero: "))

if numero1%2==0 and numero2%2==0: #se divide el numero1 entre 2 se sacar el reciduo de la divicion si el numero es igual a cero el numero es par
    print("los dos son pares")
elif numero1%2==0 and numero2%2!=0:
    print(f"{numero1} es par")
elif numero1%2!=0 and numero2%2==0:
    print(f"{numero2} es par")
elif numero1%2!=0 and numero2%2!=0:
    print("ambos numeros son impares")
