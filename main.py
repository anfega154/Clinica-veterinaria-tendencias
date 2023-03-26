from model.Persona.Persona import Persona
from model.Vendedor.aplicacion.MenuVendedor import MenuVendedor
from model.Veterinaria.Veterinaria import Veterinaria
from shared.login import login

admin = Persona("0000000", "admin", 32, "administrador", "admin", "admin")
veterinaria = Veterinaria()
veterinaria.personas.append(admin)
usuario = False
salir = False

while not salir:
    while usuario == False:
        usuario = login(veterinaria.personas)

    if usuario.rol == "administrador":
        print("codigo administrador")
    elif usuario.rol == "Veterinario":
        print("codigo Veterinario")
    elif usuario.rol == "Vendedor":
        respuesta = MenuVendedor(veterinaria)
        if respuesta == "salir":
            salir = True
        elif respuesta == "cerrar sesion":
            usuario = False


