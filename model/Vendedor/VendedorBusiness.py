import uuid
from datetime import date


from shared.rolesEnum import Roles

def venderMedicamentos(vendedor, cedula):
    for vendedor in vendedor.personas:
        if vendedor.cedula == cedula:
            return vendedor
        return False
OrdenMedica = {
        "IdOrden" : "1234",
        "idMascota": "6789",
        "CedulaDueno":"1152",
        "CedulaVeterinario": "2233"
    }
def ObtenerOrdenPorId():
     return OrdenMedica  
        

medicamentos = {
    "Desparacitante para perro: $10000": 10000,
    "Desparacitante para gato: $15000": 15000,
    "Prevención de pulgas y garrapatas: 12000": 12000,
    "Prevención del gusano del corazón: $20000": 20000,
    "Analgésico: $25000": 25000
}

def mostrar_menu():
    print("\nSeleccione el medicamento que desea comprar:")
    for i, medicamento in enumerate(medicamentos.keys(), start=1):
        print(f"{i}. {medicamento}")

def calcular_total(compras):
    total = 0
    for medicamento, cantidad in compras.items():
        precio = medicamentos[medicamento]
        total += precio * cantidad
    return total

def comprar_medicamentos():
    compras = {}
    while True:
      try:
        mostrar_menu()
        opcion = input(
            "Ingrese el número de opción del medicamento (0 para finalizar la compra): ")
        if opcion == "0":
            break
        elif opcion.isdigit() and int(opcion) in range(1, len(medicamentos) + 1):
            medicamento = list(medicamentos.keys())[int(opcion) - 1]
            cantidad = input(
                f"Ingrese la cantidad de {medicamento} que desea comprar: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                if medicamento in compras:
                    compras[medicamento] += cantidad
                else:
                    compras[medicamento] = cantidad
                print(f"{cantidad} {medicamento} x unidad agregado(s) a su compra.")
            else:
                print("Cantidad inválida. Intente nuevamente.")
        else:
            print("Opción inválida. Intente nuevamente.")
      except:
          print("Error, solo se permite numeros enteros")
    print("Carrito de compras:")
    for medicamento, cantidad in compras.items():
        print(f"{cantidad} {medicamento}")

    total = calcular_total(compras)
    print(f"Total a pagar: ${total}")

class Factura:
    def __init__(self, idMascota, cedulaDueño, nombreProducto, valor, cantidad):
        self.idFactura = str(uuid.uuid4())
        self.idMascota = str(idMascota)
        self.cedulaDueño = cedulaDueño
        self.nombreProducto = nombreProducto
        self.valor = valor
        self.cantidad = cantidad
        self.fecha = str(date.today())

    def MostrarFactura(self):
        print("*****Factura*****")
        print("Id de la factura: ",self.idFactura)
        print("Id mascota: ",self.idMascota)
        print("Cedula dueño ",self.cedulaDueño)
        print("Nombre del producto: ",self.nombreProducto)
        print("Valor a pagar: ",self.valor)
        print("Cantidad: ",self.cantidad)
        print("Fecha: ",self.fecha)

    
    





