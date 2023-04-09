#from model.Vendedor.UI.Factura import Factura

import uuid
from datetime import datetime

class OrdenMascota:
    def __init__(self, idMascota, idDueno, idVeterinario, medicamento, dosis):
        self.idOrden = str(uuid.uuid4())
        self.idMascota = idMascota
        self.idDueno = idDueno
        self.idVeterinario = idVeterinario
        self.medicamento = medicamento
        self.dosis = dosis
        self.fechaGeneracion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
    def imprimirOrden(self):
        print("\n----- ORDEN DE MASCOTA -----")
        print("ID de orden:", self.idOrden)
        print("ID de mascota:", self.idMascota)
        print("Cédula del dueño:", self.idDueno)
        print("Cédula del veterinario que ordena:", self.idVeterinario)
        print("Nombre del medicamento y dosis:", self.medicamento, self.dosis)
        print("Fecha de generación:", self.fechaGeneracion)

# Ejemplo de uso
orden = OrdenMascota("1235", "5678", "9012", "Paracetamol", "500mg")
orden.imprimirOrden()
print("")