from paciente import Paciente
from medico import Medico
from cita_medica import CitaMedica
from menu_medico import mostrar_menu2
from basedatos import cargar_citas, guardar_citas


if __name__ == "__main__":
    medico1 = Medico("Dr. Juan Perez",  "Consultorio A", "Lunes y Miércoles de 8:00 AM - 12:00 PM")
    paciente1 = Paciente("Ana Gomez", "Pediatría")
    paciente1.citas = cargar_citas()
    
    while True:
        mostrar_menu2()
        opcion = int(input("Ingrese el número de opción que desea realizar: "))

        if opcion == 1:
            citas_agendadas = medico1.consultar_Citas_Agendadas(paciente1)
            if citas_agendadas:
                print("Citas médicas agendadas:")
                for cita in citas_agendadas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas agendadas.")

        elif opcion == 2:
            citas_registradas = paciente1.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for cita in citas_registradas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 3:
            citas_agendadas = medico1.consultar_Citas_Agendadas(paciente1)
            if citas_agendadas:
                print("Citas médicas agendadas:")
                for cita in citas_agendadas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas agendadas.")

        elif opcion == 4:
            citas_registradas = paciente1.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for idx, cita in enumerate(citas_registradas):
                    print(f"{idx + 1}. {cita.obtenerInformacionCita()}")

                num_cita_eliminar = int(input("Ingrese el número de la cita que desea eliminar: "))
                if num_cita_eliminar > 0 and num_cita_eliminar <= len(citas_registradas):
                    cita_eliminar = citas_registradas[num_cita_eliminar - 1]
                    paciente1.eliminar_cita_propia(cita_eliminar)
                    print("¡Cita médica eliminada exitosamente!")
                else:
                    print("Opción inválida.")
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 5:
            guardar_citas(paciente1.citas)
            print("¡Hasta luego!")
            
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")
