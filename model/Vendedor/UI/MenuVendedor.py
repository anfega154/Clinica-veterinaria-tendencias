#from model.Vendedor.UI.VendedorBusiness import venderMedicamentos

def MenuVendedor():
    while True:
        print("\nMenú:")
        print("1. Ver Orden")
        print("2. vender medicamentos")
        print("3. registrar facturas")
        print("4. cerrar sesion")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            # ver ordenes
            print("# ver ordenes")
        elif opcion == "2":
            # vender medicamentos
            #print("# vender medicamentos")
            print("\nBienvenido. Por favor ingrese una opción: ")
            print("1. Desparacitante para perro ")
            print("2. Desparacitante para gatos ")
            print("3. Desparacitante para peces ")
            print("4. Desparacitante para aves ")
            print("5. Antiinflamatorios no esteroidales ")
            print("6. Medicamentos para el colesterol ")
            print("7. Benzodiacepina ")
            print("8. Paracetamol ")
            print("9.Salir\n")

            opc = int(input("Seleccione el medicamento a comprar: "))

            if opc == 1:
                print("Desparacitante para perro tiene un valor de 30 mil pesos \n")
                return
            if opc == 2:
                print("Desparacitante para gatos tiene un valor de 30 mil pesos \n")
                return
            if opc == 3:
                print("Desparacitante para peces tiene un valor de 10 mil pesos \n")
                return
            if opc == 4:
                print("Antiinflamatorios no esteroidales tiene un valor de 25 mil pesos \n")
                return
            if opc == 5:
                print("Medicamentos para el colesterol tiene un valor de 15 mil pesos \n")
                return
            if opc == 6:
                print("Benzodiacepina tiene un valor de 25 mil pesos \n")
                return
            if opc == 7:
                print("Paracetamol tiene un valor de 25 mil pesos \n")
                return
            if opc == 8:
                print("Paracetamol tiene un valor de 25 mil pesos \n")
                return
            if opc == 9:
                print("Saliendo... ")
                break
            else:
                print("Opción incorrecta. Por favor seleccione una opcón de nuevo.")
                return MenuVendedor()

        elif opcion == "3":
            # registrar factura
            print("registrar factura")
        elif opcion == "4":
            return "cerrar sesion"
        elif opcion == "5":
            print("Saliendo....")
            break
        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")
            return MenuVendedor()
MenuVendedor()