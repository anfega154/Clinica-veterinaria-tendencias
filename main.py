from model.Administrador.UI.MenuAdministrador import MenuAdministrador
from model.Persona.Persona import Persona
from model.Vendedor.aplicacion.MenuVendedor import MenuVendedor
from model.Veterinaria.Veterinaria import Veterinaria
from shared.login import login
from shared.rolesEnum import Roles

admin = Persona("0000000", "admin", 32, "Administrador", "admin", "admin")
veterinaria = Veterinaria()
veterinaria.personas.append(admin)
usuario = False
salir = False

while not salir:
    while usuario == False:
        usuario = login(veterinaria.personas)

    if usuario.rol == Roles.Administrador.value:
        respuesta = MenuAdministrador(veterinaria)
        if respuesta == "salir":
            salir = True
        elif respuesta == "cerrar sesion":
            usuario = False
        
    elif usuario.rol == Roles.veterinario.value:
        print("codigo Veterinario")

    elif usuario.rol == Roles.vendedor.value:
        respuesta = MenuVendedor(veterinaria)
        if respuesta == "salir":
            salir = True
        elif respuesta == "cerrar sesion":
            usuario = False


