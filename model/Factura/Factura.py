import uuid
from datetime import date

class Factura:
    def __init__(self, idMascota,idFactura, cedulaDueño, idOrden,productos, total):
        self.idFactura = idFactura
        self.idMascota = idMascota
        self.cedulaDueño = cedulaDueño
        self.idOrden = idOrden
        self.productos = productos
        self.total = total 
        self.fecha = str(date.today())
