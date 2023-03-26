def login(ListaUsuarios):
    nombreUsuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    usuarioEncontrado = None
    for usuario in ListaUsuarios:
        if usuario.nombreUsuario == nombreUsuario  and usuario.contraseña == contraseña:
            usuarioEncontrado = usuario
            print("Bienvenido: " + usuario.nombre)
            return usuario
    print("usuario o contraseña equivocados...")
    return False
    
    