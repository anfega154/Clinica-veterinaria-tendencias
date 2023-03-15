from model.Administrador import AdministradorBusiness

def addEmpleado(veterinaria,nombre,cedula,edad,rol):
    if nombre== None or nombre == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    
    if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if edad == None or edad == " ":
        print("la edad no puede ser un espacio vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    if rol == None or rol== " ":
        print("rol no puede ser un espacio vacio")
        return
    if rol !="MEDICO" or rol !="VENDEDOR":
        print("el rol debe ser MEDICO o VENDEDOR")
        return
    print("validacion exitosa")
    AdministradorBusiness.AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol)

