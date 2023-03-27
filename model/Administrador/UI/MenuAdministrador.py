
from model.Administrador.AdministradorBusiness import AfiliarEmpleado
from shared.rolesEnum import Roles


def MenuAdministrador(veterinaria):
    while True:
        print("\nBienvenido al menú de administrador. Por favor ingrese una opción: ")
        print("1. Registrar medico veterinario")
        print("2. Registrar vendedor")
        print("3. Historia medica")
        print("4. Registro de facturas")
        print("5. Consultar ordenes")
        print("6. Dueño mascota")
        print("7. Mascota")
        print("8. cerrar sesion")
        print("9. Salir")

        opc = int(input("\nIngrese una opción: "))

        if opc == 1:
            print("\nRegistrar medico veterinario")
            cedulaVeterinario = input("\nIngrese la cedula del medico veterinario: ")
            nombreVeterinario = input("\nIngrese el nombre del medico veterinario: ")
            edad = input("\nIngrese la edad del medico veterinario: ")
            rol = Roles.veterinario.value
            usuario = input("\nIngrese el usuario del medico veterinario: ")
            contraseña = input("\nIngrese la contraseña del medico veterinario: ")
            AfiliarEmpleado(veterinaria, nombreVeterinario, cedulaVeterinario, edad, rol, usuario, contraseña)

        elif opc == 2:
            print("\nRegistrar Vendedor")
            cedulaVeterinario = input("\nIngrese la cedula del vendedor: ")
            nombreVeterinario = input("\nIngrese el nombre del vendedor: ")
            edad = input("\nIngrese la edad del vendedor: ")
            rol = Roles.vendedor.value
            usuario = input("\nIngrese el usuario del vendedor: ")
            contraseña = input("\nIngrese la contraseña del vendedor: ")
            AfiliarEmpleado(veterinaria, nombreVeterinario, cedulaVeterinario, edad, rol, usuario, contraseña)

        elif opc == 3:
            print("\nSeleccionaste historia medica")

        elif opc == 4:
            print("\nSeleccionaste registro de facturas")

        elif opc == 5:
            print("\nSeleccionaste consultar ordenes")

        elif opc == 6:
            print("\nSeleccionaste sueño de mascota")

        elif opc == 7:
            print("\nSeleccionaste mascota")

        elif opc == 8:
            return "cerrar sesion"

        elif opc == 9:
            return "salir"

        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")
