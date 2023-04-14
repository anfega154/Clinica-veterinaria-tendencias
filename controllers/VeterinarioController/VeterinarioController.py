from model.DueñoMascota.DueñoMascotaBussines import AfiliarDueñoMascota, buscarCedula, ConsultarMascotasDueño
from model.Mascota.MascotaBusiness import afiliarMascota
from model.MedicoVeterinario.MedicoVeterinarioBusiness import ActualizarHistoriaClinica, ActualizarOrden, AnularOrdenPorIdOrden, BuscarOrden, BuscarOrdenPorIdMascota, CrearOrden, ObtenerHistoriaClinicaPorId, crearHistoriaClinica
from model.Administrador.AdministradorBusiness import AfiliarEmpleado,EliminarEmpleado,ActualizarEmpleado
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
    AfiliarDueñoMascota(veterinaria, nombreDueño, str(cedula), edad)

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
    if idMascota == None or idMascota == " ":
        print("Id mascotas no pueden ser un espacio vacio")
        return
    
    if profesionalAtiende == None or profesionalAtiende == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedulaProfesional = int(profesionalAtiende)
    except:
        print("la cedula debe ser numerica")
        return
    
    if motivoConsulta == None or motivoConsulta == " ":
        print("Motivo onsulta no pueden ser un espacio vacio")
        return
    
    if sintomatologia == None or sintomatologia == " ":
        print("sintomatologia no pueden ser un espacio vacio")
        return
    
    if diagnostico == None or diagnostico == " ":
        print("diagnostico no pueden ser un espacio vacio")
        return
    
    if procedimiento == None or procedimiento == " ":
        print("procedimiento no pueden ser un espacio vacio")
        return
    
    if alergiaMedicamentos == None or alergiaMedicamentos == " ":
        print("Alergia medicamentos no pueden ser un espacio vacio")
        return
    
    if detalleProcedimiento == None or detalleProcedimiento == " ":
        print("Detalle procedimiento no pueden ser un espacio vacio")
        return
    
    crearHistoriaClinica(veterinaria, idMascota, fechaConsulta, str(cedulaProfesional), motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento )
    
def consultaHistoriaClinicaDeMascota(veterinaria, id):
    return ObtenerHistoriaClinicaPorId(veterinaria,id)

def crearOrden (veterinaria, idOrden, idMascota, cedulaDueño, veterinarioCedula, medicamento, dosis, fechaConsulta, estadoOrden ):
    if idMascota == None or idMascota == " ":
        print("Id mascotas no pueden ser un espacio vacio")
        return
    
    if cedulaDueño == None or cedulaDueño == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedulaDueño)
    except:
        print("la cedula debe ser numerica")
        return
    
    if veterinarioCedula == None or veterinarioCedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedulaProfesional = int(veterinarioCedula)
    except:
        print("la cedula debe ser numerica")
        return
    
    if medicamento == None or medicamento == " ":
        print("medicamento no pueden ser un espacio vacio")
        return
    
    if dosis == None or dosis == " ":
        print("dosis no pueden ser un espacio vacio")
        return
    
    if estadoOrden == None or estadoOrden == " ":
        print("Estado orden no pueden ser un espacio vacio")
        return
    CrearOrden(veterinaria, idOrden, idMascota, cedula, cedulaProfesional, medicamento, dosis, fechaConsulta, estadoOrden)
    
def actualizarHistoriaClinica(veterinaria, idMascota, fechaConsulta, campoParaModificar, nuevoCampo):
    if fechaConsulta == None or fechaConsulta == " ":
        print("Fecha no pueden ser un espacio vacio")
        return
    
    if idMascota == None or idMascota == " ":
        print("id Mascota orden no pueden ser un espacio vacio")
        return
    
    if nuevoCampo == None or nuevoCampo == " ":
        print(f"Informacion del campo {campoParaModificar} no pueden estar vacio")
        return
    ActualizarHistoriaClinica(veterinaria,  idMascota, fechaConsulta, campoParaModificar, nuevoCampo)

def buscarOrden(veterinaria, fechaGeneracion):
    if fechaGeneracion == None or fechaGeneracion == " ":
        print("Fecha consulta no pueden ser un espacio vacio")
        return
    return BuscarOrden(veterinaria, fechaGeneracion)

def actualizarOrden(veterinaria, fechaGeneracion, campo, nuevoCampo):
    if fechaGeneracion == None or fechaGeneracion == " ":
        print("Fecha consulta no pueden ser un espacio vacio")
        return
    
    if nuevoCampo == None or nuevoCampo == " ":
        print(f"la informacion del campo {nuevoCampo} no pueden ser un espacio vacio")
        return
    ActualizarOrden(veterinaria, fechaGeneracion, campo, nuevoCampo)
    
def BuscarOrdenesDeMascota(veterinaria, idMascota):
    if idMascota == None or idMascota == " ":
        print("Id mascotas no pueden ser un espacio vacio")
        return
    return BuscarOrdenPorIdMascota(veterinaria, idMascota)

def AnularOrden(veterinaria, idOrden):
    if idOrden == None or idOrden == " ":
        print("Id orden no pueden ser un espacio vacio")
        return
    AnularOrdenPorIdOrden(veterinaria, idOrden)

def addEmpleado(veterinaria,nombre,cedula,edad,rol,usuario,contraseña):
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
    if usuario == None or usuario== " ":
        print("usuario no puede ser un espacio vacio")
        return
    if contraseña == None or contraseña== " ":
        print("usuario no puede ser un espacio vacio")
        return
    
    print("validacion exitosa")
    AfiliarEmpleado(veterinaria,nombre,cedula,edad,rol,usuario,contraseña)
    

def EliminarEmpleado(veterinaria,cedula):
   if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
   try:
        cedula = int(cedula)
   except:
        print("la cedula debe ser numerica")
        return
   EliminarEmpleado(veterinaria,cedula)


def actualizarEmpleado(veterinaria, cedula, nombre=None, edad=None, contraseña=None):
    if cedula == None or cedula == " ":
        print("la cedula no puede ser vacio")
        return
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if nombre is not None:
        nombreEmpleado = nombre
    if edad is not None:
        edadEmpledado = edad
    if contraseña is not None:
        contraseñaEmpleado = contraseña
    ActualizarEmpleado(veterinaria, cedula, nombreEmpleado, edadEmpledado, contraseñaEmpleado)