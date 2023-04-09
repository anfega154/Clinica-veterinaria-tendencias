from model.Persona.Persona import Persona

def buscarCedula(veterinaria,cedula):
     for persona in veterinaria.personas:
        if persona.cedula==cedula:
            return persona
         

def AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol,usuario,contraseña):
    cedulaEncontrada = buscarCedula(veterinaria,cedula)
    if cedulaEncontrada != None:
        print("la cedula ya esta registrada")
        return
    empleado = Persona(cedula,nombre,edad,rol, usuario, contraseña)
    veterinaria.personas.append(empleado)
    print("se ha registrado empleado con exito")

def EliminarEmpleado(veterinaria,cedula):
    cedulaEncontrada=buscarCedula(veterinaria,cedula)
    if cedulaEncontrada == None:
        print("la cedula no esta registrada")
        return
    for i in range(len(veterinaria.personas)):
        if(veterinaria.personas[i].cedula ==cedulaEncontrada.cedula):
            veterinaria.personas.pop(i)
            print("se elimino con exito")
            return
        

def ActualizarEmpleado(veterinaria, cedula, nombre=None, edad=None, contraseña=None):
    empleado = buscarCedula(veterinaria, cedula)
    if empleado is None:
        print("La cédula no está registrada")
        return
    if nombre is not None:
        empleado.nombre = nombre
    if edad is not None:
        empleado.edad = edad
    if contraseña is not None:
        empleado.contraseña = contraseña
    print("Se actualizó el empleado con éxito")
