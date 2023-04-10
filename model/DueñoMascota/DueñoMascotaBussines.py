from model.DueñoMascota.DueñoMascota import DueñoMascota


def buscarCedula(veterinaria,cedula):
    for persona in veterinaria.personas:
        if persona.cedula == cedula:
            return persona
    return False 
    
def AfiliarDueñoMascota(veterinaria,nombre,cedula,edad):
    dueñoMascota = buscarCedula(veterinaria,cedula)
    if dueñoMascota != False:
        print("la cedula ya esta registrada")
        return
    dueñoMascota = DueñoMascota(cedula,nombre,edad)
    veterinaria.personas.append(dueñoMascota)
    print("------------se ha registrado dueño de mascota con exito--------------")
    
def ConsultarMascotasDueño(veterinaria, cedula):
    dueñoMascota = buscarCedula(veterinaria,str(cedula))
    if dueñoMascota == False:
        print("la cedula no esta registrada")
        return
    return dueñoMascota.mascotas
