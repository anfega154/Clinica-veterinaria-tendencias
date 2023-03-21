from model.Administrador import AdministradorBusiness
from model.Mascota import MascotaBusiness
from model.Veterinaria import veterinaria

def addEmpleado(veterinaria,nombre,cedula,edad,rol):
    if nombre== None or nombre == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    
    if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if edad == None or edad == " ":
        print("la edad no puede ser un espacio vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    if rol == None or rol== " ":
        print("rol no puede ser un espacio vacio")
        return
    if rol !="MEDICO" or rol !="VENDEDOR":
        print("el rol debe ser MEDICO o VENDEDOR")
        return
    print("validacion exitosa")
    AdministradorBusiness.AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol)

def addMascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso,id):
    if nombre== None or nombre == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    if cedula_dueño == None or cedula_dueño == " ":
        print("la edad no puede ser un espacio vacio")
        return
    try:
        cedula_dueño = int(cedula_dueño)
    except:
        print("la cedula debe ser numerica")
        return
    if edad == None or edad == " ":
        print("la edad no puede ser un espacio vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    if especie== None or especie == " ":
        print("la especie no puede ser un espacio vacio")
        return
    if raza== None or raza == " ":
        print("la raza no puede ser un espacio vacio")
        return
    if caracteristicas== None or caracteristicas == " ":
        print("las caracteristicas no puede ser un espacio vacio")
        return
    
    if peso == None or peso == " ":
        print("la edad no puede ser un espacio vacio")
        return
    
    id= len(veterinaria.mascotas)

    MascotaBusiness.afiliarMascota(nombre, cedula_dueño, edad, especie, raza, caracteristicas, peso,id)



    