
from controllers.VeterinarioController.VeterinarioController import addEmpleado,EliminarEmpleado,actualizarEmpleado
from shared.rolesEnum import Roles


def MenuAdministrador(veterinaria):
    while True:
        print("\nBienvenido al menú de administrador. Por favor ingrese una opción: ")
        print("1. Registrar medico veterinario")
        print("2. Registrar vendedor")
        print("3. Eliminar Un perfil")
        print("4. Actualizar usuario")
        print("5. cerrar sesion")
        print("6. Salir")

        opc = input("\nIngrese una opción: ")

        if opc == "1":
            print("\nRegistrar medico veterinario")
            cedulaVeterinario = input(
                "\nIngrese la cedula del medico veterinario: ")
            nombreVeterinario = input(
                "\nIngrese el nombre del medico veterinario: ")
            edad = input("\nIngrese la edad del medico veterinario: ")
            rol = Roles.veterinario.value
            usuario = input("\nIngrese el usuario del medico veterinario: ")
            contraseña = input(
                "\nIngrese la contraseña del medico veterinario: ")
            addEmpleado(veterinaria, nombreVeterinario,
                            cedulaVeterinario, edad, rol, usuario, contraseña)

        elif opc == "2":
            print("\nRegistrar Vendedor")
            cedulaVendedor = input("\nIngrese la cedula del vendedor: ")
            nombreVendedor = input("\nIngrese el nombre del vendedor: ")
            edad = input("\nIngrese la edad del vendedor: ")
            rol = Roles.vendedor.value
            usuario = input("\nIngrese el usuario del vendedor: ")
            contraseña = input("\nIngrese la contraseña del vendedor: ")
            addEmpleado(veterinaria, nombreVendedor,
                            cedulaVendedor, edad, rol, usuario, contraseña)

        elif opc == "3":
            print("\nEliminar un perfil")
            cedula = input("\nIngrese el numero de la cedula a eliminar: ")
            EliminarEmpleado(veterinaria, cedula)

        elif opc == "4":
            print("\nActualizar Usuario")
            cedula = input("\nIngrese la cedula del vendedor: ")
            nombre = input("\nIngrese el nombre del vendedor: ")
            edad = input("\nIngrese la edad del vendedor: ")
            contraseña = input("\nIngrese la contraseña del vendedor: ")
            actualizarEmpleado(veterinaria,cedula, nombre,  edad ,contraseña)

        elif opc == "5":
            return "cerrar sesion"

        elif opc == "6":
            return "salir"

        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")
