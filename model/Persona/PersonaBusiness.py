
def buscarCedula(veterinaria,cedula):
    for persona in veterinaria.personas:
        if persona.cedula==cedula:
            return persona
    return False    
