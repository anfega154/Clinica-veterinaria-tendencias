import random
import datetime

class Factura ():
    def __init__(self, idMascota, idDueno, idOrden, nombreProducto, valor, cantidad ):
        self.idFactura = self.generar_id_factura()
        self.idMascota = idMascota
        self.idDueno = idDueno
        self.idOrden = idOrden
        self.nombreProducto = nombreProducto
        self.valor = valor
        self.cantidad = cantidad
        self.fecha = self.generar_fecha_actual()

    def generar_id_factura(self):
        idFactura = ''.join(random.choices("0123456789ABCDEF",k=8)) 
        return idFactura

    def generar_fecha_actual(self):
        fecha_actual = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return fecha_actual

    def mostrar_factura(self):
        # Displays the invoice details
        print("\nId factura: ", self.idFactura)
        print("Id mascota: ", self.idMascota)
        print("Id dueño: ", self.idDueno)
        print("Id orden: ", self.idOrden)
        print("Nombre del producto: ", self.nombreProducto)
        print("Valor: $", self.valor)
        print("Cantidad: $", self.cantidad)
        print("Fecha: ", self.fecha)
        print()

# Ejemplo:
idMascota = "12345"
idDueno = "56789"
idOrden = "98765"
nombreProducto = "Acetaminofen"
valor = 10.99
cantidad = 12.99

# Crear una factura
factura = Factura(idMascota, idDueno, idOrden, nombreProducto, valor, cantidad)

# Mostrar los detalles de la factura
factura.mostrar_factura() 