def venderMedicamentos(vendedor, cedula):
    for vendedor in vendedor.personas:
        if vendedor.cedula == cedula:
            return vendedor
        return False

# Definir un diccionario de medicamentos con sus precios
medicamentos = {
    "Desparacitante para perro: $10000": 10000,
    "Desparacitante para gato: $15000": 15000,
    "Prevención de pulgas y garrapatas: 12000": 12000,
    "Prevención del gusano del corazón: $20000": 20000,
    "Analgésico: $25000": 25000
}

# Función para mostrar el menú de opciones


def mostrar_menu():
    print("\nSeleccione el medicamento que desea comprar:")
    for i, medicamento in enumerate(medicamentos.keys(), start=1):
        print(f"{i}. {medicamento}")

# Función para calcular el total a pagar


def calcular_total(compras):
    total = 0
    for medicamento, cantidad in compras.items():
        precio = medicamentos[medicamento]
        total += precio * cantidad
    return total

# Función principal del programa


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


# Llamar a la función principal desde aqui
#comprar_medicamentos()