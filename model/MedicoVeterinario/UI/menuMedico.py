from datetime import datetime
from controllers.VeterinarioController.VeterinarioController import AgregarMascota, AnularOrden, BuscarOrdenesDeMascota, CrearHistoriaClinica, AgregarDueñoMascota, BuscarDueñoMascota, actualizarHistoriaClinica, actualizarOrden, buscarMascotaDeDueño, consultaHistoriaClinicaDeMascota, crearOrden
from model.MedicoVeterinario.MedicoVeterinarioBusiness import AfiliarDueñoMascota, buscarCedula
from shared.especiesEnum import Especies
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
        print("8. Consultar orden")
        print("9. Anular orden")
        print("10. cerrar sesion")
        print("11. Salir")
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            print("\nRegistrar dueño de la mascota")
            cedulaDueño = input(
                "\nIngrese la cedula del dueño de la mascota: ")
            nombreDueño = input(
                "\nIngrese el nombre del dueño de la mascota: ")
            edad = input("\nIngrese la edad del dueño de la mascota: ")
            rol = Roles.dueñoMascota.value
            AgregarDueñoMascota(veterinaria, cedulaDueño,
                                nombreDueño, edad, rol)

        elif opc == 2:
            print("\nBuscar dueño de mascota")
            cedulaDueño = input(
                "\nIngrese la cedula del dueño de la mascota: ")
            duenoMascota = BuscarDueñoMascota(veterinaria, cedulaDueño)
            if duenoMascota == False:
                print("no se encontro el dueño de la mascota")
            print("La cedula le pertenece a:")
            print(duenoMascota)

        elif opc == 3:
            print("\nRegistrar mascota")
            idMascota = uuid.uuid4()
            nombreMascota = input("\nIngrese el nombre de la mascota: ")
            cedulaDueño = input(
                "\nIngrese la cedula del dueño de la mascota: ")
            edadMascota = input("\nIngrese la edad de la mascota: ")
            
            while True:
                print("Especie de la mascota")
                print("1. Canino")
                print("2. Felino")
                print("3. Otro")
                try:
                    opcionEspecie = int(input("Ingrese una opción: "))
                except:
                    print("la opcion debe de ser un numero entre 1 y 3")
                    continue
                if opcionEspecie < 1 or opcionEspecie > 3:
                    print("no es una opcion valida")
                elif opcionEspecie == 1:
                    especie = Especies.Canino.value
                    break
                elif opcionEspecie == 2:
                    especie = Especies.Felino.value
                    break
                elif opcionEspecie == 3:
                    especie = input("Cual?: " )
                    break
                
            raza = input("\nIngrese la raza de la mascota: ")
            caracteristicas = input(
                "\nIngrese las caracteristicas de la mascota: ")
            peso = input("\nIngrese el peso de la mascota: ")
            AgregarMascota(veterinaria, duenoMascota, nombreMascota, cedulaDueño,
                           edadMascota, especie, raza, caracteristicas, peso, idMascota)

        elif opc == 4:
            print("\nConsultar mascota")
            cedulaDueño = input(
                "\nIngrese la cedula del dueño de la mascota: ")
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)

        elif opc == 5:
            print("\nCrear historia clinica")
            cedulaDueño = input(
                "\nIngrese la cedula del dueño de la mascota: ")
            mascotas = buscarMascotaDeDueño(veterinaria, cedulaDueño)
            print("\nCual de las siguientes mascotas es la que recibirá la consulta?")

            for indice, mascotaDelDueño in enumerate(mascotas):
                print(
                    f"indice: {indice} identificacion mascota: {mascotaDelDueño.id} nombre mascota: {mascotaDelDueño.nombre}")

            while True:
                indice = int(
                    input("Ingrese el indice de la mascota que realiza la consulta: "))
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
            diagnostico = input("Diagnostico Medico: ")

            while True:
                try:
                    tieneProcedimiento = int(input(
                        "Se realizara algun procedimiento a la mascota? 1: Sí, 0: No "))
                    if tieneProcedimiento < 0 or tieneProcedimiento > 1:
                        print("El valor debe de ser 1 o 0")
                    else:
                        break
                except:
                    print("la opcion debe de ser un valor numerico: ")
                    continue

            if tieneProcedimiento == 1:
                while True:
                    print("que procedimiento desera realizar?")
                    print("1. desparasitación")
                    print("2. fisioterapia")
                    print("3. vacunación")
                    print("4. examenes")
                    print("5. cirugía")
                    print("6. otro")
                    try:
                        procedimiento= int(input("selecione el procedimiento: "))
                        if procedimiento < 1 and procedimiento > 6:
                            print ("opcion invalida")
                    except:
                        print("el valor debe de ser numerico")
                        continue
                    if procedimiento == 1:
                        procedimiento = "desparasitación"
                        break
                    elif procedimiento == 2:
                        procedimiento = "fisioterapia"
                        break
                    elif procedimiento == 3:
                        procedimiento = "vacunación"
                        break
                    elif procedimiento == 4:
                        procedimiento = "examenes"
                        break
                    elif procedimiento == 5:
                        procedimiento = "cirugía"
                        break
                    elif procedimiento == 6:
                        procedimiento = input("¿Cual?: ")
                        break
            else:
                procedimiento = "ninguno"
                
            alergiaMedicamentos = input("Medicamentos a los que es alergica la mascota: ")
            detalleProcedimiento = input("detalles del procedimiento: ")
            while True:
                try:
                    tieneMedicación = int(input(
                        "Se realizara medicación para la mascota? 1: Sí, 0: No "))
                    if tieneMedicación < 0 or tieneMedicación > 1:
                        print("La opcion no es valida, debe ingresar 1 o 0")
                    else:
                        break
                except:
                    print("la opcion debe de ser un numero entre 1 y 2")
                    continue
                
            if tieneMedicación == 1:
                medicamento= input("Medicamento: ")
                dosis= input("dosis: ")
                idOrden= str(uuid.uuid4())
                estadoOrden = "Activa"
                crearOrden(veterinaria, idOrden, idMascota, cedulaDueño, veterinario.cedula, medicamento, dosis, fechaConsulta, estadoOrden)
            else:
                medicamento = "ninguno"
                dosis = "ninguno"
                idOrden= "sin orden"
                estadoOrden = "sin orden"
            
            if procedimiento == 3 and (mascota.especie == "Canino" or mascota.especie == "Felino" ):
                vacunas = input("Nombre de la vacuna: ")
            else:
                vacunas = "Ninguna"
                
            CrearHistoriaClinica(veterinaria, idMascota, fechaConsulta, profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento )
            
            for key, value in veterinaria.historiaClinica.items():
                print(key + ":", value)
                
            for key, value in veterinaria.ordenes.items():
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
            print("\nEditar historia clinica")
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
                print(f"Estado de la Orden: {registro['estado_orden']}")
                print("------------------------------------------------------------")
           
           
            while True:
                print("que campo desea editar?")
                print("1. motivo_consulta: ")
                print("2. sintomatologia: ")
                print("3. diagnostico: ")
                print("4. procedimiento: ")
                print("5. medicamento: ")
                print("6. dosis_medicamento: ")
                print("7. vacunacion: ")
                print("8. alergias_medicamentos: ")
                print("9. detalle_procedimiento: ")
                print("10. dejar de editar: ")
                
                try:
                    opcionEditar = int(input("Ingrese el numero del campo que desea actualizar"))
                except:
                    print("la copcion debe de ser un numero entre el 1 y el 11")
                    continue
                if opcionEditar == 1:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevoMotivoConsulta = input("Ingrese el nuevo motivo de consulta")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "motivo_consulta", nuevoMotivoConsulta)
                elif opcionEditar == 2:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevaSintomatologia = input("Ingrese la sintomatologia")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "sintomatologia", nuevaSintomatologia)
                elif opcionEditar == 3:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevDiagnostico = input("Ingrese el diagnostico")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "diagnostico", nuevDiagnostico)
                elif opcionEditar == 4:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevoProcedimiento = input("Ingrese el procedimiento")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "procedimiento", nuevoProcedimiento)
                elif opcionEditar == 5:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevoMedicamento = input("Ingrese la informacion del/los medciamento/s")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "medicamento", nuevoMedicamento)
                    actualizarOrden(veterinaria, fechaConsulta, "medicamentos", nuevoMedicamento)
                elif opcionEditar == 6:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevaDosis = input("Ingrese la informacion de la dosis")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "medicamento", nuevaDosis)
                    actualizarOrden(veterinaria, fechaConsulta, "dosis", nuevaDosis)
                elif opcionEditar == 7:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevaVacunacion = input("Ingrese la vacuna")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "vacunacion", nuevaVacunacion)
                elif opcionEditar == 8:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevaAlergiasMedicamento = input("Ingrese las alergias a medicamentos")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "alergias_medicamentos", nuevaAlergiasMedicamento)
                elif opcionEditar == 9:
                    fechaConsulta = input("copie y pegue la fecha de la HC a la cual desea editar")
                    nuevoDetalleProcedimiento = input("Ingrese los detalles del procedimiento")
                    actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "detalle_procedimiento", nuevoDetalleProcedimiento)
                elif opcionEditar == 10:
                    break
                else:
                    print("Opcion no valida")
                
        elif opc == 8:
            print("\nConsultar Orden")
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

        elif opc == 9:
            print("\nAnular Orden")
            print("\nConsultar Orden")
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
            
            ordenes = BuscarOrdenesDeMascota(veterinaria, mascota.id)
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
                    ordenParaAnular = int(input("digite el indice de la orden que desea anular: "))
                    if ordenParaAnular < 0 or ordenParaAnular > len(ordenes):
                        print("el indice que digito no es valido")
                        return
                    else:
                        orden = ordenes[0]
                        idOrden = orden["id_orden"]
                        fechaConsulta = orden["fecha_generacion"]
                        break
                except:
                    print("Debe ingresar un valor numerico")
                    continue
            AnularOrden(veterinaria, idOrden)
            actualizarHistoriaClinica(veterinaria, str(mascota.id), fechaConsulta, "estado_orden", "Anulado")
        elif opc == 10:
            return "cerrar sesion"
        elif opc == 11:
            return "salir"
        else:
            print("Opción inválida. Intente de nuevo.")

