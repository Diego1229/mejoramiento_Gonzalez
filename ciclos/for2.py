# construye un programa que reciba como datos el peso la altura y el genero de N personas, obtenga el promedio del peso
# y el promedio de la altura, tanto de la poblacion masculina como de la femenina
comprobar = True
while comprobar == True:
   N = int(input("ingrese la cantidad de personas a evaluar "))

   if N > 0:
        comprobar = False
    
        peso_hombres = 0   # aqui se almacena la sumatoria de el peso de todos los hombre, igual acendentemente.
        altura_hombres = 0
        peso_mujeres= 0
        altura_mujeres= 0
        cantidad_hombres= 0
        cantidad_mujeres= 0
    
        for i in range (N):
            peso= float(input("ingrese el peso en Kg"))
            altura= float(input("ingrese la altura en Cm"))
            genero= input("ingrese el genero de la persona (M) (F): ")
    
            if genero.upper() == "M":
                peso_hombres += peso 
                altura_hombres += altura 
                cantidad_hombres += 1
        
            elif genero.upper() == "F":
                peso_mujeres += peso
                altura_mujeres += altura
                cantidad_mujeres += 1
            else:
                print("el genero no es correcto. Intente nuevamente")
        
        promedio_pesoH = 0
        promedio_alturaH = 0

        if cantidad_hombres > 0:
               
           promedio_pesoH = peso_hombres / cantidad_hombres       
           promedio_alturaH = altura_hombres / cantidad_hombres
        
        promedio_pesoM= 0
        promedio_alturaM = 0
       
        if cantidad_mujeres > 0:    

            promedio_pesoM = peso_mujeres / cantidad_mujeres
            promedio_alturaM = altura_mujeres / cantidad_mujeres

            print("\nDe los datos optenidos los promedios son: " 
                "\nPromedio  peso de hombres",promedio_pesoH,
                "\nPromedio altura de hombres",promedio_alturaH,
                "\nPromedio peso de mujeres",promedio_pesoM,
                "\nPromedio altura mujeres",promedio_alturaM)
   else:
        print("el numero ingresado no es correcto, intentelo de nuevo. ")
