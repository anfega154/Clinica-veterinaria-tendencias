personas = {}

def registrar_cliente(cedula,nombre,edad):
    if cedula in personas:
        print(f"Error, el cliente con cedula {cedula} ya existe")

    if cedula == None or cedula =="":
        print("La cedula no puede ser un campo vacio")
        return
    
    if nombre == None or nombre =="":
        print("El nombre no puede ser un espacio vacio")
        return
    
    if edad == None or edad == "":
        print("La edad no puede ser vacio")
        return

    try:
        cedula = int(cedula)
    except:
        print("La cedula debe ser numerica")
        return
    
    try:
        edad = int(edad)
    except:
        print("La edad debe ser numerica")
        return
    
    else:
        personas[cedula] = {"nombre": nombre, "edad": edad}
        print(f"El cliente con cedula {cedula} ha sido registrado exitosamente")
        registrar_cliente(cedula,nombre,edad)
