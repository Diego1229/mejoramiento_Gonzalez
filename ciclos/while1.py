
x = int(input("Por favor, digita tu edad para poder entrar a la fiesta: "))

while x <= 0 or x >= 100:
     print("edad incorrectaa. intentalo nuevamente")
     x = int(input("Por favor, digita tu edad para poder entrar a la fiesta: "))
 
       
if x >= 18:
     print("Eres mayor de edad y puedes entrar a la fiesta.")
    
else:
    print("eres menor de edad y no puedes entrar a la fiesta .")
       