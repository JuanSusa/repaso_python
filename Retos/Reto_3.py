# Nombre, Materia, Teléfono

instructores2557861 = {}

while True:
    print("¡¡Bienvenido!!")
    print("1. Añadir/Modificar.")
    print("2. Buscar.")
    print("3. Borrar.")
    print("4. Listar.")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))   
    if opcion == 1:
        inst = input("Ingrese el nombre del instructor: \n")
        if inst in instructores2557861:
            print("El instructor ya se encuentra registrado en la ficha.")
            opcion1 = int(input("Digite 1 si desea modificar nombre del instructor. \nDigite 2 si desea modificar la materia del instructor de la ficha. \nDigite 3 si desea modificar el teléfono del instructor. \n"))
            if opcion1 == 1:
                nombre = input("Ingrese el nuevo nombre del instructor. \n")
                instructores2557861 ['Nombre'] = nombre
            elif opcion1 == 2:
                materia = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861 [inst]['Materia'] = materia
            elif opcion1 == 3:
                telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
                instructores2557861 [inst]['Teléfono'] = telefono
            else:
                print("¡¡ERROR!! Opción no valida.")
        
        else:
            print("El instructor no se encuentra en el sistema.")
            opAgregar = int(input("Seleccione una opcion: \n"
                              "1. Para Agregar\n"
                              "2. Para Salir \n"))
            if opAgregar == 1:
                instructores2557861[inst] = {}
                nameInstru = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861[inst] ['Nombre']= inst
                materia = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861[inst]['Materia'] = materia
                telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
                instructores2557861[inst]['Telefono'] = telefono
                print(instructores2557861)
                break