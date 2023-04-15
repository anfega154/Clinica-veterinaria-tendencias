from model.Mascota.Mascota import Mascota

def buscarCedula(veterinaria, cedula):
    objetos_en_cadena = map(str, veterinaria.personas)
    print(list(objetos_en_cadena))
    for persona in veterinaria.personas:
        if persona.cedula == cedula:
            return persona
    return False


def afiliarMascota(veterinaria, nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso, id):
    personaEncontrada = buscarCedula(veterinaria, cedula_dueño)
    if personaEncontrada == False:
        print("No se encontro cedula del dueño")
        return False

    mascota = Mascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso, id)
    veterinaria.mascotas.append(mascota)
    print("--------------Se registro con exito-------------")
    return mascota





