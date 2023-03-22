class Persona:
    def __init__(self, cedula, nombre, edad, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.rol = rol

    def get_tipo(self):
        return self.rol

    def es_Vendedor(self):
        return self.rol == "Vendedor"

    def es_DueñoMascota(self):
        return self.rol == "DueñoMascota"

    def es_MedicoVeterinario(self):
        return self.rol == "MedicoVeterinario"