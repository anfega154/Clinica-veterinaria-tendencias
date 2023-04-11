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
     