"""Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores"""

def calcular_nota(nota):   # se definela funcion, recibe como parametro 'nota'
   
   if nota == 10 or nota ==9:         #comprobar la nota para teterminar el mendaje apropiado       
      return"felicitacines exelente nota"
   elif nota == 8 or nota == 7:
      return"buena nota "
   elif nota == 6 or nota == 5:
       return"obtuvo una nota suficiente para pasar"
   elif nota >10 or nota !=0:
      return "es una nota no valida"   
   
   else:
      return"usted perdio el trimestre"   

nota=int(input("ingrese su nota: ")) #la nota la proporciona el usuario

mensaje= calcular_nota(nota) #se llama la funcio calcular nota con el valor 'nota' y se guarda el resultado en la variable 'mensaje'

print(mensaje ) # se imprime mensaje resultante  