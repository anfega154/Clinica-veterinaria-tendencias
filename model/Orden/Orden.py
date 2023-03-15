from model.Persona.Persona import Persona

class OrdenMascotas(Persona):   
    def __init__(self, cedula, nombre, edad, rol):
        super().__init__(cedula, nombre, edad, rol)
        self.cedula
