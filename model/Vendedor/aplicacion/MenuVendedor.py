def MenuVendedor(usuario):
    while True:
        print("\nMenú:")
        print("1. Ver Orden")
        print("2. vender medicamentos")
        print("3. registrar facturas")
        print("4. cerrar sesion")
        print("5. Salir")
        opcion = input("Elija una opción:")

        if opcion == "1":
            # ver ordenes
            print("# ver ordenes")
        elif opcion == "2":
            # vender medicamentos
            print("vender medicamentos")
        elif opcion == "3":
            # registrar factura
            print("registrar factura")
        elif opcion == "4":
            # cerrar sesion
            print("cerrar sesion")
        elif opcion == "5":
            # salir
            print("salir")
            return
        else:
            print("opcion no valida")

