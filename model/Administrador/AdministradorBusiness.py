from model.Persona.Persona import Persona

def buscarCedula(veterinaria,cedula):
     for persona in veterinaria.personas:
        if persona.cedula==cedula:
            return persona
        return False 

def AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol, usuario, contraseña):
    cedulaEncontrada = buscarCedula(veterinaria,cedula)
    if cedulaEncontrada != False:
        print("la cedula ya esta registrada")
        return
    empleado = Persona(cedula,nombre,edad,rol, usuario, contraseña)
    veterinaria.personas.append(empleado)
    print("se ha registrado empleado con exito")
