import VendedorBusiness

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
            print(VendedorBusiness.comprar_medicamentos())  

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
        
#MenuVendedor()
