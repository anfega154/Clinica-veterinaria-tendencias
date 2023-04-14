import uuid
from datetime import date
from model.DueñoMascota.DueñoMascotaBussines import AfiliarDueñoMascota, buscarCedula
from shared.rolesEnum import Roles


def venderMedicamentos(vendedor, cedula):
    for vendedor in vendedor.personas:
        if vendedor.cedula == cedula:
            return vendedor
        return False

medicamentos = {
    "Desparacitante_perros": 10000,
    "Desparacitante_gato": 15000,
    "Prevención_pulgas": 12000,
    "Prevención_garrapatas": 20000,
    "Aspirina": 2500,
    "Acetaminofen": 1500,
    "Suero":5000,
    "Amoxicilina": 20000,
    "Gotas_Ojos": 40000

}

def mostrar_menu():
    print("\nSeleccione el medicamento que desea comprar:")
    for key, value in medicamentos.items():
                        print(key + ":", value)

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
    
    compras_string = ""
    for medicamento, cantidad in compras.items():
        compras_string += f"{cantidad} {medicamento}, "
    compras_string = compras_string[:-2] + "."

    print("Carrito de compras:")
    print(compras_string)

    total = calcular_total(compras)
    print(f"Total a pagar: ${total}")
    return compras
         
    
def BuscarOrden(veterinaria, fechaGeneracion):
     for orden in veterinaria.ordenes.values():
          if orden['fecha_generacion'] == fechaGeneracion:
              return orden
          else:
               return False
          
def BuscarOrdenPorIdMascota(veterinaria, idMascota):
     ordenes_por_mascota = []
     for orden in veterinaria.ordenes.values():
          if orden['id_mascota'] == idMascota:
               ordenes_por_mascota.append(orden)
     return ordenes_por_mascota

def BuscarOrdenPorIdOrden(veterinaria, idOrden):
     for orden in veterinaria.ordenes.values():
          if orden['id_orden'] == idOrden:
              return orden
          else:
               return False  
          
"""    for edicamentos in enumerate(medicamentos.keys(), start=1):
        print(key + ":", value) """





