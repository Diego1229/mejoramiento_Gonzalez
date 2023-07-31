from paciente import Paciente
from medico import Medico
from cita_medica import CitaMedica
from Menu_paciente import mostrar_menu
from basedatos import cargar_citas, guardar_citas

if __name__ == "__main__":
    medico2 = Medico("Dr. juan manuel", "Consultorio b", "miercoles y viernes de 8:00 AM - 5:00 PM")
    paciente2 = Paciente("diego", "medico general" )
    paciente2.citas = cargar_citas()

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de opción que desea realizar: "))

        if opcion == 1:
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la cita (HH:MM AM/PM): ")
            motivo = input("Ingrese el motivo de la cita: ")
            especialista = input("Ingrese la especialidad del médico que necesita: ")
            cita_nueva = CitaMedica(paciente2, medico2, fecha, hora, motivo)
            medico2.especialidad = especialista
            paciente2.registrar_cita(cita_nueva)
           

            print("¡Cita médica registrada exitosamente!")

        elif opcion == 2:
            citas_registradas = paciente2.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for cita in citas_registradas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 3:
            citas_agendadas = medico2.consultar_Citas_Agendadas()
            if citas_agendadas:
                print("Citas médicas agendadas:")
                for cita in citas_agendadas:
                    print(cita.obtenerInformacionCita())
            else:
                print("No tiene citas médicas agendadas.")

        elif opcion == 4:
            citas_registradas = paciente2.consultar_citas_registradas()
            if citas_registradas:
                print("Citas médicas registradas:")
                for idx, cita in enumerate(citas_registradas):
                    print(f"{idx + 1}. {cita.obtenerInformacionCita()}")

                num_cita_eliminar = int(input("Ingrese el número de la cita que desea eliminar: "))
                if num_cita_eliminar > 0 and num_cita_eliminar <= len(citas_registradas):
                    cita_eliminar = citas_registradas[num_cita_eliminar - 1]
                    paciente2.eliminar_cita_propia(cita_eliminar)
                    print("¡Cita médica eliminada exitosamente!")
                else:
                    print("Opción inválida.")
            else:
                print("No tiene citas médicas registradas.")

        elif opcion == 5:
            guardar_citas(paciente2.citas)
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")
