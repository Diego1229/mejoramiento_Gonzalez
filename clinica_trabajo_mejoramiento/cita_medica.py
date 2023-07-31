class CitaMedica():
    def __init__(self, paciente, medico, fecha, hora, motivo):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def obtenerInformacionCita(self):
        return f"Paciente: {self.paciente.nombre}, Médico: {self.medico.nombre}, Especialidad: {self.medico.especialidad}, Fecha: {self.fecha}, Hora: {self.hora}, Motivo: {self.motivo}"
