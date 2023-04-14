from model.Administrador.AdministradorBusiness import AfiliarEmpleado,EliminarEmpleado,ActualizarEmpleado

def addEmpleado(veterinaria,nombre,cedula,edad,rol,usuario,contraseña):
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
    if usuario == None or usuario== " ":
        print("usuario no puede ser un espacio vacio")
        return
    if contraseña == None or contraseña== " ":
        print("usuario no puede ser un espacio vacio")
        return
    
    print("validacion exitosa")
    AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol,usuario,contraseña)
    

def deleteEmpleado(veterinaria,cedula):
   if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
   try:
        cedula = int(cedula)
   except:
        print("la cedula debe ser numerica")
        return
   EliminarEmpleado(veterinaria,cedula)


def actualizarEmpleado(veterinaria, cedula, nombre=None, edad=None, contraseña=None):
    if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if nombre is not None:
        nombreEmpleado = nombre
    if edad is not None:
        edadEmpledado = edad
    if contraseña is not None:
        contraseñaEmpleado = contraseña
    ActualizarEmpleado(veterinaria, cedula, nombreEmpleado, edadEmpledado, contraseñaEmpleado)