from model.Persona.Persona import Persona
from shared.rolesEnum import Roles

class DueñoMascota(Persona):
    mascotas = []
    def __init__(self, cedula, nombre, edad):
        super().__init__(cedula, nombre, edad, Roles.dueñoMascota.value)

