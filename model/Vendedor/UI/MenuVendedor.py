from model.Vendedor.VendedorBusiness import comprar_medicamentos
from controllers.VendedorConttroller.VendedorController import ConsultarOrden
from controllers.VeterinarioController.VeterinarioController import buscarMascotaDeDueño


def MenuVendedor(veterinaria):
    while True:
        print("\nMenú:")
        print("1. Ver Orden")
        print("2. vender medicamentos")
        print("3. registrar facturas")
        print("4. cerrar sesion")
        print("5. Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            # ver ordenes
            print("\nConsulta orden medica")
            
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ") 
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)
            print("\nA cual de las siguientes mascotas desea consultar la orden?")
            
            for indice, mascotaDelDueño in enumerate(mascotas):
                print(f"indice: {indice} identificacion mascota: {mascotaDelDueño.id} nombre mascota: {mascotaDelDueño.nombre}")
            
            while True:
                indice = int(input("Ingrese el indice de la mascota que realiza la consulta de la orden: "))
                if indice < 0 or indice >= len(mascotas):
                    print("opcion invalida no corresponde al indice de las mascotas")
                    return
                mascota = mascotas[indice]
                break
            
            OrdenMedica = ConsultarOrden()
            
            for key, value in OrdenMedica.items():
                print(key + ":", value)

        elif opcion == 2:
            # vender medicamentos
            print(comprar_medicamentos())  

        elif opcion == 3:
            # registrar factura
            print("registrar factura")
        elif opcion == 4:
            return "cerrar sesion"
        elif opcion == 5:
            return "salir"
        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")

