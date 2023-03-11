from model.Persona.Persona import Persona

class DueñoMascota(Persona):
    def __init__(self, cedula, nombre, edad):
        super().__init__(cedula, nombre, edad, "DueñoMascota")