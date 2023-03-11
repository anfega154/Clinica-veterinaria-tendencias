from model.Persona.Persona import Persona

class Administrador(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "Administrador")
        self.usuario = usuario
        self.contrasena = contrasena