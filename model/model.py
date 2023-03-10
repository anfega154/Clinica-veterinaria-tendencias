from datetime import date
class Veterinaria:
    def __init__(self):
        self.personas = [] 
        self.mascotas = [] 
        self.facturas = []

class Persona:
    def __init__(self, cedula, nombre, edad, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.rol = rol


class MedicoVeterinario(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "MedicoVeterinario")
        self.usuario = usuario
        self.contrasena = contrasena

class Administrador(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "Administrador")
        self.usuario = usuario
        self.contrasena = contrasena

class DueñoMascota(Persona):
    def __init__(self, cedula, nombre, edad):
        super().__init__(cedula, nombre, edad, "DueñoMascota")

class Vendedor(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "Vendedor")
        self.usuario = usuario
        self.contrasena = contrasena

class Mascota:
    def __init__(self, nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso):
        self.nombre = nombre
        self.cedula_dueño = cedula_dueño
        self.edad = edad
        self.id = None 
        self.especie = especie
        self.raza = raza
        self.caracteristicas = caracteristicas
        self.peso = peso

class HistoriaClinica:
    def __init__(self, id_mascota, fecha, medico, motivo, sintomatologia, diagnostico,
                  procedimiento, medicamento, dosis, id_orden):
        self.id_mascota=id_mascota
        self.fecha=fecha
        self.medico=medico
        self.motivo=motivo
        self.sitomatologia=sintomatologia
        self.diagnostico=diagnostico
        self.procedimiento=procedimiento
        self.medicamento=medicamento
        self.dosis=dosis
        self.id_orden=id_orden
