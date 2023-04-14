import uuid
from datetime import date

class Factura:
    def __init__(self, idMascota, cedulaDueño, productos, total):
        self.idFactura = str(uuid.uuid4())
        self.idMascota = str(idMascota)
        self.cedulaDueño = cedulaDueño
        self.productos = productos
        self.total = total 
        self.fecha = str(date.today())
