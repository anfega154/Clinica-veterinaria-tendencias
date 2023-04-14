from datetime import datetime
import uuid

class OrdenMascotas:  
    def __init__(self, idMascota, cedulaDueno, cedulaVeterinario,nombreMedicamento):
     self.idOrden = str(uuid.uuid4())
     self.idMascota = idMascota
     self.cedulaDueno = cedulaDueno
     self.cedulaVeterinario = cedulaVeterinario
     self.nombreMedicamento = nombreMedicamento
     self.fechaHistoria = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
