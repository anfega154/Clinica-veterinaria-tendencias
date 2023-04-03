
def venderMedicamentos(vendedor,cedula):
     for vendedor in vendedor.personas:
        if vendedor.cedula==cedula:
            return vendedor
        return False 