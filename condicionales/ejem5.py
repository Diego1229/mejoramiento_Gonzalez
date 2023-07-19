"""hacer un programa que permita que el estudiante ingrese su nota optenida en su evaluacion
    si la nota es menor que 5 reprueva el semestre"""

nota= int(input("ingrese la nota optenia del parcial: "))

if nota>0 and nota<6:
    if nota<5:
          print("reprobo")
    if nota==5:
          print("aprobo") 
else:
    print("nota erronea")
