from model.Persona.Persona import Persona

class MedicoVeterinario(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "MedicoVeterinario")
        self.usuario = usuario
        self.contrasena = contrasena