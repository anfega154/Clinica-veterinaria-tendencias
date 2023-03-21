from model.Veterinaria import veterinaria
from model.Mascota import Mascota


def afiliarMascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso, id):
    if buscarCedula(veterinaria, cedula_dueño) == False:
        print("No se encontro cedula del dueño, valide")
        return

    mascota = Mascota(nombre, cedula_dueño, edad, especie,
                      raza, caracteristicas, peso, id)
    veterinaria.mascostas.append(mascota)
    print("Se registro con exito")


def buscarCedula(veterinaria, cedula_dueño):
    for persona in veterinaria.personas:
        if persona.cedula == cedula_dueño:
            return persona
        return False
    


