"""hacer un programa que le pida el salario a un profesor , calcule el  """
"""incremento del salario de acuerdo con los siguientes criterios y escriba el nuevo salario del profesor """

#salario < 18.000 => incremento 12%
#$18,000 <= salario <= $30,000 => incremento 8%.
#$30,000 < salario <- $50,000 => incremento 7%.
#$50,000 < salario => incremento 6%.


salario = float(input("ingrese el salario pofesor: "))
if salario < 18.000:
    salario += (salario * 0.12)
    print(f"el nuevo salario del profesor es{salario}")

elif 18.000 <= salario <= 30.000 :
    salario += (salario * 0.08)
    print(f"el nuevo salario del profesor es{salario}")

elif 30.000 < salario <= 50.000:
    salario += (salario * 0.07) 
    print(f"el nuevo salario del profesor es{salario}")

else:
    salario += (salario * 0.06)
    print(f"el nuevo salario del profesor es{salario}")