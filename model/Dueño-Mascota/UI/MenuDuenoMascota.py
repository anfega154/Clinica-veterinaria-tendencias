
def MenuDueñoMascotas():
    opc = 0
    while opc !=6:
        print("1. Datos de tu mascota")
        print("2. Historia clinica de tu mascota")
        print("3. Orden de tu mascota")
        print("4. Comprar productos para tu mascota")
        print("5. Mostrar factura")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opc == 1:
            print("Menu caquita")
        elif opc == 2:
            print("Ese chocorramito cual es")
        elif opc == 3:
            print("Mira el chocorramito que destape")
        elif opc == 4:
            print("Ese pastel de pollo cual es")
        elif opc == 5:
            print("Ya me puedo dormir?")
            break
        else:
            print("Opción inválida. Intente de nuevo.")