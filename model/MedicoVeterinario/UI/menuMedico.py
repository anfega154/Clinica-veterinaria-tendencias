from datetime import datetime
from controllers.VeterinarioController.VeterinarioController import AgregarMascota, CrearHistoriaClinica, AgregarDueñoMascota, BuscarDueñoMascota, buscarMascotaDeDueño, consultaHistoriaClinicaDeMascota
from model.MedicoVeterinario.MedicoVeterinarioBusiness import AfiliarDueñoMascota, buscarCedula
from shared.rolesEnum import Roles
import uuid


def menuMedicoVeterinario(veterinaria, veterinario):
    opc = -1
    duenoMascota = None
    mascota = None

    while opc != 0:
        print("1. Registar el dueño de la mascota")
        print("2. Consultar el dueño de la mascota")
        print("3. Registrar mascota")
        print("4. Consultar mascota")
        print("5. Crear Historia Clinica")
        print("6. Consultar Historia Clinica")
        print("7. Editar Historia clinica")
        print("8. Crear orden")
        print("9. Consultar orden")
        print("10 Anular orden")
        print("11. cerrar sesion")
        print("12. Salir")
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            print("\nRegistrar dueño de la mascota")
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ")
            nombreDueño = input("\nIngrese el nombre del dueño de la mascota: ")
            edad = input("\nIngrese la edad del dueño de la mascota: ")
            rol = Roles.dueñoMascota.value
            AgregarDueñoMascota(veterinaria, cedulaDueño, nombreDueño, edad, rol)
            
        elif opc == 2:
            print("\nBuscar dueño de mascota")
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ")
            duenoMascota = BuscarDueñoMascota(veterinaria, cedulaDueño)
            if duenoMascota == False :
                print("no se encontro el dueño de la mascota")
            print("La cedula le pertenece a:")
            print(duenoMascota)
            
        elif opc == 3:
            print("\nRegistrar mascota")
            idMascota = uuid.uuid4()
            nombreMascota = input("\nIngrese el nombre de la mascota: ")
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ")
            edadMascota = input("\nIngrese la edad de la mascota: ")
            especie = input("\nIngrese la especie de la mascota: ")
            raza = input("\nIngrese la raza de la mascota: ")
            caracteristicas = input("\nIngrese las caracteristicas de la mascota: ")
            peso = input("\nIngrese el peso de la mascota: ")
            AgregarMascota(veterinaria, duenoMascota, nombreMascota, cedulaDueño, edadMascota, especie, raza, caracteristicas, peso, idMascota)
            
            
        elif opc == 4:
            print("\nConsultar mascota")
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ") 
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)
            
            
        elif opc == 5:
            print("\nCrear historia clinica")
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ") 
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)
            print("\nCual de las siguientes mascotas es la que recibirá la consulta?")
            
            for indice, mascotaDelDueño in enumerate(mascotas):
                print(f"indice: {indice} identificacion mascota: {mascotaDelDueño.id} nombre mascota: {mascotaDelDueño.nombre}")
            
            while True:
                indice = int(input("Ingrese el indice de la mascota que realiza la consulta: "))
                if indice < 0 or indice >= len(mascotas):
                    print("opcion invalida no corresponde al indice de las mascotas")
                    return
                mascota = mascotas[indice]
                break
            
            print("**************************************************************")
            print(f"creacion de historia clinica para {mascota.nombre}")
            
            fechaConsulta = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            profesionalAtiende = veterinario.nombre
            idMascota = str(mascota.id)
            motivoConsulta = input("Motivo por el que consulta: ")
            sintomatologia = input("Sintomatologia de las mascota: ")
            diagnostico= input("Diagnostico Medico: ")
            procedimiento= input("procedimiento que se realizo: ")
            medicamento= input("Medicamento: ")
            dosis= input("dosis: ")
            idOrden= str(uuid.uuid4())
            estadoOrden = "Activa"
            vacunas = input("Nombre de la vacuna: ")
            alergiaMedicamentos = input("Medicamentos a los que es alergica la mascota: ")
            detalleProcedimiento = input("detalles del procedimiento: ")
            
            
            CrearHistoriaClinica(veterinaria, idMascota, fechaConsulta, profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento )
            
            for key, value in veterinaria.historiaClinica.items():
                print(key + ":", value)
                
        elif opc == 6:
            print("\nConsulta historia clinica")
            
            cedulaDueño = input("\nIngrese la cedula del dueño de la mascota: ") 
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)
            print("\nA cual de las siguientes mascotas desea consultar la historia clinica?")
            
            for indice, mascotaDelDueño in enumerate(mascotas):
                print(f"indice: {indice} identificacion mascota: {mascotaDelDueño.id} nombre mascota: {mascotaDelDueño.nombre}")
            
            while True:
                indice = int(input("Ingrese el indice de la mascota que realiza la consulta d ela historia clinica: "))
                if indice < 0 or indice >= len(mascotas):
                    print("opcion invalida no corresponde al indice de las mascotas")
                    return
                mascota = mascotas[indice]
                break
            
            historiaClinica = consultaHistoriaClinicaDeMascota(veterinaria, str(mascota.id))
            print("*****************************************************")
            print("*************HISTORIA CLINICA************************")
            for fecha, registro in historiaClinica.items():
                print(f"Fecha: {fecha}")
                print(f"Medico Veterinario: {registro['medico_veterinario']}")
                print(f"Motivo de Consulta: {registro['motivo_consulta']}")
                print(f"Sintomatología: {registro['sintomatologia']}")
                print(f"Diagnóstico: {registro['diagnostico']}")
                print(f"Procedimiento: {registro['procedimiento']}")
                print(f"Medicamento: {registro['medicamento']}")
                print(f"Dosis de Medicamento: {registro['dosis_medicamento']}")
                print(f"ID de Orden: {registro['ID_orden']}")
                print(f"Historial de Vacunación: {registro['historial_vacunacion']}")
                print(f"Alergias a Medicamentos: {registro['alergias_medicamentos']}")
                print(f"Detalle del Procedimiento: {registro['detalle_procedimiento']}")
                print(f"Anulación de Orden: {registro['estado_orden']}")
                print("------------------------------------------------------------")
            
            
        elif opc == 7:
            print("here: "+str(opc))
        elif opc == 8:
            print("here: "+str(opc))
        elif opc == 9:
            print("here: "+str(opc))
        elif opc == 11:
            return "cerrar sesion"
        elif opc == 12:
            return "salir"
        else:
            print("Opción inválida. Intente de nuevo.")

