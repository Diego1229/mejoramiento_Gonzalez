from paciente import Paciente
from medico import Medico
from cita_medica import CitaMedica

def guardar_citas(citas):
    with open('citas.txt', 'w') as file:
        for cita in citas:
            file.write(f"{cita.paciente.nombre}|{cita.medico.nombre}|{cita.medico.especialidad}|{cita.fecha}|{cita.hora}|{cita.motivo}\n")

def cargar_citas():
    try:
        with open('citas.txt', 'r') as file:
            lineas = file.readlines()
            citas = []
            for linea in lineas:
                datos = linea.strip().split('|')
                paciente = Paciente(datos[0], datos[1])
                medico = Medico(datos[2], datos[3], datos[4])  # Corregir los argumentos aquí
                cita = CitaMedica(paciente, medico, datos[5], datos[6], datos[7])
                citas.append(cita)
            return citas
    except FileNotFoundError:
        return []
    