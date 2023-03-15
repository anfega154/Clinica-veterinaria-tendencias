from model.Persona import persosna
from model.Veterinaria import veterinaria

def AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol):
    if buscarCedula(veterinaria,cedula)!=False:
        print("la cedula ya esta registrada")
        return
    empleado=persosna(cedula,nombre,edad,rol)
    veterinaria.personas.append(empleado)
    print("se ha registrado empleado con exito")

def buscarCedula(veterinaria,cedula):
    for persona in veterinaria.personas:
        if persona.cedula==cedula:
            return persona
    return False    