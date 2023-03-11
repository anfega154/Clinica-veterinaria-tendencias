class Vendedor(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, "Vendedor")
        self.usuario = usuario
        self.contrasena = contrasena