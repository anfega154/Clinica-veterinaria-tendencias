from model.DueñoMascota.DueñoMascotaBussines import AfiliarDueñoMascota, buscarCedula, ConsultarMascotasDueño
from model.Mascota.MascotaBusiness import afiliarMascota
from model.MedicoVeterinario.MedicoVeterinarioBusiness import ObtenerHistoriaClinicaPorId, crearHistoriaClinica
from shared.rolesEnum import Roles


def AgregarDueñoMascota(veterinaria, cedulaDueño, nombreDueño, edad, rol):
    if nombreDueño == None or nombreDueño == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    
    if cedulaDueño == None or cedulaDueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedulaDueño)
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
    print("------------validacion exitosa---------------------")
    AfiliarDueñoMascota(veterinaria, nombreDueño, cedula, edad)

def BuscarDueñoMascota(veterinaria, cedula):
    if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    return buscarCedula(veterinaria, cedula)

def AgregarMascota(veterinaria, dueñoMascota, nombre, cedulaDueño, edad, especie, raza, caracteristicas, peso,id):

    if nombre == None or nombre == " ":
        print("el nombre no puede ser un espacio vacio")
        return
    
    if cedulaDueño == None or cedulaDueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedulaDueño)
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
    
    if especie == None or especie == " ":
        print("la especie no puede ser un espacio vacia")
        return
    
    if raza == None or raza == " ":
        print("la raza no puede ser un espacio vacia")
        return
    
    if caracteristicas == None or caracteristicas == " ":
        print("las caracteristicas no pueden ser un espacio vacio")
        return
    
    if peso == None or peso == " ":
        print("el peso no puede ser un espacio vacio")
        return
    try:
        peso = int(peso)
    except:
        print("el peso debe ser numerica")
        return
    
    print("------------validacion exitosa---------------------")
    mascota = afiliarMascota(veterinaria, nombre, cedulaDueño, edad, especie, raza, caracteristicas, peso, id)
    
    if dueñoMascota == None:
        dueñoMascota = buscarCedula(veterinaria, cedulaDueño)
    
    print(dueñoMascota)
    dueñoMascota.mascotas.append(mascota)
    
def buscarMascotaDeDueño(veterinaria, cedulaDueño):
    if cedulaDueño == None or cedulaDueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedulaDueño)
    except:
        print("la cedula debe ser numerica")
        return
    return ConsultarMascotasDueño(veterinaria, cedula)

def CrearHistoriaClinica(veterinaria, idMascota, fechaConsulta, profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento ):
    crearHistoriaClinica(veterinaria, idMascota, fechaConsulta, profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento )
    
def consultaHistoriaClinicaDeMascota(veterinaria, id):
    return ObtenerHistoriaClinicaPorId(veterinaria,id)
    
    
    
