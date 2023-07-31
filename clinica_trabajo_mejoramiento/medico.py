#from usuario import Usuario
class Medico():
    def __init__(self, nombre, consultorio, horario_disponible):
        self.nombre = nombre
        self.especialidad = None
        self.consultorio = consultorio
        self.horario_disponible = horario_disponible
        self.citas_agendadas = []

    def consultar_Citas_Agendadas(self,paciente):
         citas_paciente = [cita for cita in self.citas_agendadas if cita.paciente == paciente]
         return citas_paciente

    def definirHorarioDisponible(self, horario):
        self.horario_disponible = horario

    def eliminarCita(self, cita):
        if cita in self.citas_agendadas:
            self.citas_agendadas.remove(cita)

