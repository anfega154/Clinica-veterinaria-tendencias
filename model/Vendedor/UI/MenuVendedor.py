from controllers.VendedorConttroller.VendedorController import Crear_factura
from model.Vendedor.VendedorBusiness import comprar_medicamentos
import uuid
from controllers.VeterinarioController.VeterinarioController import buscarMascotaDeDueño, BuscarOrdenesDeMascota
from model.Factura.FacturaBusiness import crear_factura

def MenuVendedor(veterinaria):
    compras = None
    while True:
        print("\nMenú:")
        print("1. Ver Orden")
        print("2. vender medicamentos para personas registradas")
        print("3. vender medicamentos para personas no registradas")
        print("4. cerrar sesion")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
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
            
            ordenes = BuscarOrdenesDeMascota(veterinaria, str(mascota.id))
            i = 0
            for orden in ordenes:
                print("***************************************************************")
                print("ORDEN CON INDICE: ", i)
                print("ID Orden: ", orden['id_orden'])
                print("ID Mascota: ", orden['id_mascota'])
                print("Cedula dueño: ", orden['cedula_dueño'])
                print("Cedula veterinario: ", orden['cedula_veterinario'])
                print("Medicamentos: ", orden['medicamentos'])
                print("Dosis: ", orden['dosis'])
                print("Fecha generacion: ", orden['fecha_generacion'])
                print("Estado de la orden: ", orden['estado_orden'])
                print("*************************************************************")
                i = i + 1

        elif opcion == "2":
            print("\nVenta de medicamentos para personas registradas")
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
            
            ordenes = BuscarOrdenesDeMascota(veterinaria, str(mascota.id))
            i = 0
            for orden in ordenes:
                print("Indice: ", i)
                print("ID Orden: ", orden['id_orden'])
                print("ID Mascota: ", orden['id_mascota'])
                print("Cedula dueño: ", orden['cedula_dueño'])
                print("Cedula veterinario: ", orden['cedula_veterinario'])
                print("Medicamentos: ", orden['medicamentos'])
                print("Dosis: ", orden['dosis'])
                print("Fecha generacion: ", orden['fecha_generacion'])
                i = i + 1
            
            while True:
                try:
                    ordenParaAnular = int(input("digite el indice de la orden que desea comprar: "))
                    if ordenParaAnular < 0 or ordenParaAnular > len(ordenes):
                        print("el indice que digito no es valido")
                        return
                    else:
                        orden = ordenes[ordenParaAnular]
                        idOrden = orden["id_orden"]
                        break
                except:
                    print("Debe ingresar un valor numerico")
                    continue
            compras = comprar_medicamentos() 

            print("\nGeneracion de factura")   
            Crear_factura(cedulaDueño,compras, mascota.id, idOrden, veterinaria)

        elif opcion == "3":
            print("\nVenta de medicamentos para personas no registradas")  
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ") 
            idMascota = "Ninguno"
            idOrden = "Ninguno"
            compras = comprar_medicamentos() 

            print("\nGeneracion de factura")   
            Crear_factura(cedulaDueño,compras, idMascota, idOrden, veterinaria)
            
            
           

        elif opcion == "4":
            return "cerrar sesion"
        elif opcion == "5":
            return "salir"
        else:
            print("Opción invalida. Por favor seleccione una opcón de nuevo.")

