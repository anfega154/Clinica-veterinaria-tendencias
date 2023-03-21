def menuMedicoVeterinario():
    opc = -1

    while opc != 0:
        print("1. Registar Dueño")
        print("2. Consultar Dueño")
        print("3. Registrar mascota")
        print("4. Consultar mascota")
        print("5. Consultar Historia Clinica")
        print("6. Editar Historia clinica")
        print("7. Crear orden")
        print("8. Consultar orden")
        print("9 Anular orden")
        print("0. Salir")
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            print("here: "+str(opc))
        elif opc == 2:
            print("here: "+str(opc))
        elif opc == 3:
            print("here: "+str(opc))
        elif opc == 4:
            print("here: "+str(opc))
        elif opc == 5:
            print("here: "+str(opc))
        elif opc == 6:
            print("here: "+str(opc))
        elif opc == 7:
            print("here: "+str(opc))
        elif opc == 8:
            print("here: "+str(opc))
        elif opc == 9:
            print("here: "+str(opc))
        elif opc == 0:
            print("goodBye")
        else:
            print("Opción inválida. Intente de nuevo.")

