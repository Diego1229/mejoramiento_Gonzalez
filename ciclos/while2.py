"""8. Determinar cuales son los múltiplos de 5 comprendidos entre
1 y N."""

def multiplos_de_cinco(n):
    i = 1
    while i <= n:
        if i % 5 == 0:
            print(i)
        i += 1

N = int(input("Ingrese un número: "))
print("Los múltiplos de 5 comprendidos entre 1 y", N, "son:")
multiplos_de_cinco(N) # se llama la funcion, con el valor ingresado por el usuario como argumento 
                      #Esto mostrará los múltiplos de 5 en el rango de 1 a 'n'