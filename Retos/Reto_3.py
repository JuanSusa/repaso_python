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
        nomInst = input("Ingrese el nombre del instructor: \n")
        if nomInst in instructores2557861:
            print("El instructor ya se encuentra registrado en la ficha.")
            opcion1 = int(input("Digite 1 si desea modificar nombre del instructor. \nDigite 2 si desea modificar la materia del instructor de la ficha. \nDigite 3 si desea modificar el teléfono del instructor. \n"))
            if opcion1 == 1:
                nombre = input("Ingrese el nuevo nombre del instructor. \n")
                instructores2557861 ['Nombre'] = nombre
            elif opcion1 == 2:
                materia = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861 [nomInst]['Materia'] = materia
            elif opcion1 == 3:
                telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
                instructores2557861 [nomInst]['Teléfono'] = telefono
            else:
                print("¡¡ERROR!! Opción no valida.")
        
        else:
            print("El instructor no se encuentra en el sistema.")

            opAgregar = int(input("Seleccione una opcion: \n"
                              "1. Para Agregar\n"
                              "2. Para Salir \n"))
            while opAgregar == 1:
                if opAgregar == 1:
                    instructores2557861[nomInst] = {}
                    # nameInstru = input("Ingrese el nombre del instructor a guardar. \n")
                    # instructores2557861[nomInst] ['Nombre']= nomInst
                    materia = input("Ingrese la nueva materia del instructor. \n")
                    instructores2557861[nomInst]['Materia'] = materia
                    telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
                    instructores2557861[nomInst]['Telefono'] = telefono
                    print(f"**** Se ha agregado con éxito **** {instructores2557861}")
                elif opAgregar == 2:
                    print("Gracias por utilizar nuestros servicios")
                else:
                    print("Opción invalida!")
                break
    elif opcion == 2:
        buscarInst = input("ingrese el nombre del instructor que desea buscar: \n")
        for (nomInst, datos) in instructores2557861.items():
            if nomInst.startswith(buscarInst):
                print(f"**** El instructor buscado tiene las siguientes asignaturas: {materia}  y el número de contacto es: {telefono} ****")

    elif opcion == 3:
        deleteInst = input("Ingrese el nombre del intructor que desea eliminar: \n")
        if deleteInst in instructores2557861:
            del instructores2557861[deleteInst]
            print(f"Se ha eliminado con éxito el instructor: {deleteInst}")
        else:
                print(f"El intructor {deleteInst} no existe en la base de datos.")

    elif opcion == 4:
        # for (nomInst, datos) in instructores2557861.items():
        #     print(nomInst, "->", datos)
        for i in instructores2557861:
            print(f"En la base de datos de los intructores guardados se encuentra {i} con la materia {instructores2557861[i]['Materia']} y con numero de contacto {instructores2557861[i]['Telefono']}")
    
    elif opcion == 5:
        print("Adios")
        break
    
    else:
        print("¡¡ERROR!! Opcion no valida.")    