print("MENÚ".center(20,"-"))
print("1. Regitrar medico veterinario\n"+
      "2. Regitrar vendedor\n"+
      "3. Historia clinica\n"+
      "4. Registro de facturas\n"+
      "5. Consultar ordenes\n"+
      "5. Dueño de mascota\n"+
      "5. Mascota\n"+
      "6. Ir a otro perfil\n"+
      "7. Salir\n")

opc = input("Ingrese una opción (1-7): ")

if(opc.isdigit() and int(opc) in range(1,7)):
    opcion = int(opc)
    print(f"Seleccionaste la opción {opcion}\n")
else:
    print("Error, opción invalido\n")