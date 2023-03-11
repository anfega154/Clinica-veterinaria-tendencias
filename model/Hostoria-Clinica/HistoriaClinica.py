class HistoriaClinica:
    def __init__(self, id_mascota, fecha, medico, motivo, sintomatologia, diagnostico,
                  procedimiento, medicamento, dosis, id_orden):
        self.id_mascota=id_mascota
        self.fecha=fecha
        self.medico=medico
        self.motivo=motivo
        self.sitomatologia=sintomatologia
        self.diagnostico=diagnostico
        self.procedimiento=procedimiento
        self.medicamento=medicamento
        self.dosis=dosis
        self.id_orden=id_orden