from model.Factura.FacturaBusiness import crear_factura
from model.Vendedor.VendedorBusiness import BuscarOrden


def buscarOrden(veterinaria, fechaGeneracion):
    return BuscarOrden(veterinaria, fechaGeneracion)

def Crear_factura(cedulaDueño,compras, idMascota, idOrden, veterinaria):
    crear_factura(cedulaDueño,compras, idMascota, idOrden, veterinaria)


