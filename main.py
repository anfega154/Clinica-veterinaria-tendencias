
from model.Administrador.UI.MenuAdministrador import MenuAdministrador
from model.MedicoVeterinario.UI.menuMedico import menuMedicoVeterinario
from model.Persona.Persona import Persona
from model.Vendedor.UI.MenuVendedor import MenuVendedor
from model.Veterinaria.Veterinaria import Veterinaria
from model.DueñoMascota.DueñoMascota import DueñoMascota
from shared.login import login
from shared.rolesEnum import Roles


admin = Persona("0000000", "admin", 32, "Administrador")
admin.registrarUsuarioYContraseña("admin", "admin")

veterinario1 = Persona("1152189806", "uberney", 32, Roles.veterinario.value)
veterinario1.registrarUsuarioYContraseña("uzapatap", "realmadrid")
dueño1 = DueñoMascota("123456", "camila", 24)
veterinaria = Veterinaria()
veterinaria.personas.append(admin)
veterinaria.personas.append(veterinario1)
veterinaria.personas.append(dueño1)
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
        respuesta = menuMedicoVeterinario(veterinaria, usuario)
        if respuesta == "salir":
            salir = True
        elif respuesta == "cerrar sesion":
            usuario = False

    elif usuario.rol == Roles.vendedor.value:
        respuesta = MenuVendedor(veterinaria)
        if respuesta == "salir":
            salir = True
        elif respuesta == "cerrar sesion":
            usuario = False


