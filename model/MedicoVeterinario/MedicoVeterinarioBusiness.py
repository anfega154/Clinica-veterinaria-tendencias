from model.DueñoMascota.DueñoMascotaBussines import AfiliarDueñoMascota, buscarCedula

def buscarCedula(veterinaria,cedula):
     buscarCedula(veterinaria,cedula);
    
def AfiliarDueñoMascota(veterinaria,nombre,cedula,edad,rol):
    AfiliarDueñoMascota(veterinaria,nombre,cedula,edad,rol)
    
def crearHistoriaClinica(veterinaria, idMascota, fechaConsulta, profesionalAtiende, motivoConsulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, idOrden, estadoOrden, vacunas, alergiaMedicamentos, detalleProcedimiento ):
     if idMascota not in veterinaria.historiaClinica:
          veterinaria.historiaClinica[idMascota] = {}
     veterinaria.historiaClinica[idMascota][fechaConsulta] = {
          'medico_veterinario': profesionalAtiende,
          'motivo_consulta': motivoConsulta,
          'sintomatologia': sintomatologia,
          'diagnostico': diagnostico,
          'procedimiento': procedimiento,
          'medicamento': medicamento,
          'dosis_medicamento': dosis,
          'ID_orden': idOrden,
          'historial_vacunacion': vacunas,
          'alergias_medicamentos': alergiaMedicamentos,
          'detalle_procedimiento': detalleProcedimiento,
          'estado_orden': estadoOrden
     }
     print("----------------historia clinica creada con exito!!!----------------")
     
def ObtenerHistoriaClinicaPorId(veterinaria, id):
     return veterinaria.historiaClinica[id]

def CrearOrden (veterinaria, idOrden, idMascota, cedulaDueño, veterinarioCedula, medicamento, dosis, fechaConsulta):
     if idOrden not in veterinaria.ordenes:
          veterinaria.ordenes[idOrden] = {}
     veterinaria.ordenes[idOrden] = {
          'id_orden': idOrden,
          'id_mascota': idMascota,
          "cedula_dueño": cedulaDueño,
          "cedula_veterinario": veterinarioCedula,
          "medicamentos": medicamento,
          "dosis": dosis,
          "fecha_generacion": fechaConsulta
     }
     print("-------------------------Orden Creada----------------------------")
     
def ActualizarHistoriaClinica(veterinaria,  idMascota, fechaConsulta, campoParaModificar, nuevoCampo):
     historiaClinica = veterinaria.historiaClinica[idMascota][fechaConsulta]
     historiaClinica[campoParaModificar] = nuevoCampo
     
     