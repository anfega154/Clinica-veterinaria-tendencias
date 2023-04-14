import uuid
from datetime import datetime

class Veterinaria:
    historiaClinica = {}
    def __init__(self):
        self.personas = [] 
        self.mascotas = [] 
        self.facturas = []
        self.orden = []

    def ordenMascota(self,idMascota,cedulaDueno,CedulaVeterinario,dosis):
        self.idOrden = str(uuid.uuid4())
        self.idMascota = idMascota
        self.cedulaDueno = cedulaDueno
        self.CedulaVeterinario = CedulaVeterinario
        self.dosis = dosis
        self.fechaGeneracion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def imprimirOrden(self):
        print("\n-----Orden mascota-----")
        print("Id de orden: ",self.idOrden)
        print("Id de la mascota ",self.idMascota)
        print("Cedula del dueño de la mascota: ",self.cedulaDueno)
        print("Cedula del medico meterinario que receta: ",self.CedulaVeterinario)
        print("Dosis: ",self.dosis)
        print("Fecha de generación: ",self.fechaGeneracion)

        

