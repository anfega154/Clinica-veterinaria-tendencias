def venderMedicamentos(vendedor, cedula):
    for vendedor in vendedor.personas:
        if vendedor.cedula == cedula:
            return vendedor
        return False
    
#def Ventas(medicamentos):
medicamentos = {"Desparacitante para perro: $25000": 25000,
                "Desparacitante para gato: $20000": 20000,
                "Prevención de pulgas y garrapatas: $30000": 30000,
                "Prevención del gusano del corazón: $35000": 35000,
                "Analgésico: $8000": 8000}
compras = []


while True:
    print("\n¿Qué medicamento desea comprar? ")
    print("1. Desparacitante para perro: $25000 ")
    print("2. Desparacitante para gato: $20000 ")
    print("3. Prevención de pulgas y garrapatas: $30000 ")
    print("4. Prevención del gusano del corazón: $35000 ")
    print("5. Analgésico: $8000 ")
    print("6. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
            compras.append("Desparacitante para perro: $25000")
            print("Se ha agregado desparacitante para perro a su compra\n")
    elif opcion == 2:
            compras.append("Desparacitante para gato: $20000")
            print("Se ha agregado desparacitante para gato a su compra\n")
    elif opcion == 3:
            compras.append("Prevención de pulgas y garrapatas: $30000")
            print("Se ha agregado prevención de pulgas y garrapatas a su compra\n")
    elif opcion == 4:
            compras.append("Prevención del gusano del corazón: $35000")
            print("Se ha agregado prevención del gusano del corazón a su compra\n")
    elif opcion == 5:
            compras.append("Analgésico: $8000")
            print("Se ha agregado analgésico a su compra\n")
    elif opcion == 6:
        break
    else:
            print("Opción incorrecta, por favor ingrese un número del 1 al 6")
total = 0
for medicamento in compras:
    total += medicamentos[medicamento]

print("\nEl total de su compra es: $"+str(total)+ " mil pesos")
print("")

