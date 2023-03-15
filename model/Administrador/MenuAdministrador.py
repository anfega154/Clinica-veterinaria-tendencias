
def MenuAdministrador():
    while True:
        print("\nBienvenido al menú de administrador. Por favor ingrese una opción: ")
        print("1. Registrar medico veterinario")
        print("2. Registrar vendedor")
        print("3. Historia medica")
        print("4. Registro de facturas")
        print("5. Consultar ordenes")
        print("6. Dueño mascota")
        print("7. Mascota")
        print("8. Ir a otro perfil")
        print("9. Salir")

        opc = input("\nIngrese una opción: ")

        if opc == '1':
            print("\nSeleccionaste medico meterinario")

        elif opc == '2':
            print("\nSeleccionaste vendedor")

        elif opc == '3':
            print("\nSeleccionaste historia medica")

        elif opc == '4':
            print("\nSeleccionaste registro de facturas")

        elif opc == '5':
            print("\nSeleccionaste consultar ordenes")

        elif opc == '6':
            print("\nSeleccionaste sueño de mascota")

        elif opc == '7':
            print("\nSeleccionaste mascota")

        elif opc == '8':
            print("\nSeleccionaste ir a otro perfil")

        elif opc == '9':
            print("\nSaliendo...")
            break

        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")

MenuAdministrador()