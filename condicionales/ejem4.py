"""En un juego de preguntas a las que se responde “Si” o “No” gana quien
responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de Colombia fue en el año 1810?
3. The Doors fue un grupo de rock Americano?
"""
def jugar_preguntas():
    num_preguntas = 3 #ponemos una variable con el numero total de preguntas 

    aciertos = 0 # aciertos es un contador que almacena la cantidad de acieertos 

    for i in range(1, num_preguntas + 1): #creamos un bucle para recorrer las preguntas 
        print("Pregunta", i)  #se imprime el numero de preguntas actuales

        if i == 1:  #se configura las respuestas para cada valor de i
            
            pregunta = "¿Colón descubrió América?"
            respuesta = "si"
        elif i == 2:
            pregunta = "¿La independencia de Colombia fue en el año 1810?"  
            respuesta = "si"
        elif i == 3:
            pregunta = "¿The Doors fue un grupo de rock americano?"
            respuesta = "si"

        print(pregunta) #imprimimos la pregunta actual
        respuesta_usuario = input("Tu respuesta: ").lower()

        if respuesta_usuario == "si" or respuesta_usuario == "no": # # Verificar si la respuesta es "si" o "no"
            if respuesta_usuario == respuesta: #  Comprobar si la respuesta del usuario es correcta
                print("¡Respuesta correcta!")
                aciertos += 1
            else:
                print("Respuesta incorrecta.")
        else:
            print("Respuesta inválida. Por favor, responde 'sí' o 'no.'")
        print()

    # Imprimir un mensaje al final del juego con la cantidad de aciertos
    print("Juego terminado.")
    print("Has acertado", aciertos, "preguntas de", num_preguntas, "preguntas.")

jugar_preguntas()# Llamar a la función para iniciar el juego de preguntas