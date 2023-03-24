from model.Orden import OrdenMascotas

def crear_orden(idOrden, idMascota, cedulaDueno, cedulaVeterinario,nombreMedicamento, fechaHistoria):
    if idOrden == None or idOrden == "":
        print("El id orden no puede ser vacio")
    return

    try:
        idOrden = int(idOrden)
    except:
        print("El id orden debe ser numerico")

    if idMascota == None or idMascota == "":
        print("El id mascota no puede ser vacio")
    return

    try:
        idMascota = int(idMascota)
    except:
        print("El id mascota debe ser numerico")

    if cedulaDueno == None or cedulaDueno == "":
        print("La cedula no puede ser vacio")
    return

    try:
        cedulaDueno = int(cedulaDueno)
    except:
        print("La cedula debe ser numerico")

    if cedulaVeterinario == None or cedulaVeterinario == "":
        print("La cedula no puede ser vacio")
    return

    try:
        cedulaVeterinario = int(cedulaVeterinario)
    except:
        print("La cedula debe ser numerico")

    if nombreMedicamento == None or nombreMedicamento == "":
        print("El nombre del medicamento no puede ser vacio")
    return

    if fechaHistoria == None or fechaHistoria == "":
        print("la fecha de la historia no puede ser vacio")
    return

    try:
        fechaHistoria = int(fechaHistoria)
    except:
        print("La fecha debe ser numerica")

    else:
        print("Orden creada exitosamente...")