from model.Factura.Factura import Factura
import uuid
from datetime import date


def MostrarFactura (idMascota,cedulaDueño,medicamentos,total):
        print("*****Factura*****")
        print("Id de la factura: ",str(uuid.uuid4()))
        print("Id mascota: ", idMascota)
        print("Cedula dueño ", cedulaDueño)
        print("Nombre del producto: ", medicamentos)
        print("Valor a pagar: ",total)
        print("Fecha: ",str(date.today())) 