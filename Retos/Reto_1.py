#Programa que permita agregrar, modificar y eliminar un valor de la lista, en este caso se hara una lista de instrutores

op = 1
instructores = ['jennifer', 'jhonatan', 'andres' ]

while op == 1:
    eleccion = int(input("Menu de opciones: "
                         "1. Agregar Instructor \n"
                         "2. Eliminar Instructor \n"
                         "3. Modificar Instructor \n"
                         "4. Buscar un instrutor en la lista\n"
                         "5. Enlistar \n"
                         "6. Ordenar la lista alfabeticamente\n"
                         "7. Salir\n"))
    
    if eleccion == 1:
        instructores.append(input("Ingrese el nombre del instructor que desea agregar a la lista: \n"))
        print(f"Se ha agregado correctamente el nombre del instructor a la lista\n {instructores}")
    
    elif eleccion == 2:
        opDelet = int(input("Elija la opcion que desee para poder eliminar un instructor: \n"
                            "1. Por su nombre\n"
                            "2. Por posicion especifica en la lista\n"
                            "3. Eliminar el ultimo registro de la lista\n"
                            "4. Eliminar toda la lista completa\n"))
        if opDelet == 1:
            nombre = input("Ingrese el nombre del instructor que desea eliminar: \n")
            instructores.remove(nombre)
            print(f"Se ha eliminado el instructor {nombre} de la lista")
            print(instructores)
        elif opDelet == 2:
            for index, l in enumerate (instructores):
                print(index, l)
            posicion = int(input("Ingrese la posicion del instructor que desea eliminar: \n"))
            del instructores[posicion]
            print(f"Se ha eliminado el instructor en la posicion {posicion} de la lista")
            print(instructores)
        elif opDelet == 3:
            instructores.pop()
            print(f"Se ha eliminado el ultimo registro de la lista")
            print(instructores)
        elif opDelet== 4:
            #del intructores
            instructores.clear()
            print(f"Se ha eliminado la lista completa")
            print(instructores)
    
    elif eleccion == 3:
        for index, l in enumerate (instructores):
            print(index, l)
            posicionMod = int(input("Ingrese la posicion del instructor que desea modificar: \n"))
            nombreMod = input("Ingrese el nombre del instructor que desea modificar: \n")
            instructores[posicionMod] = nombreMod
            print(f"Se ha modificado el instructor en la posicion {posicionMod} de la lista \n{instructores}")
    elif eleccion == 4:
        nameBuscar = input("Ingrese el nombre del instructor que desea buscar: \n")
        nameBuscar = nameBuscar.lower()
        if nameBuscar in instructores:
            print(f"El instructor {nameBuscar} se encuentra en la lista")
        else:
            print(f"El instructor {nameBuscar} no se encuentra en la lista")
    elif eleccion == 5:
        for index, l in enumerate (instructores):
                print(index, l)
    elif eleccion == 6:
        print(f"La lista completa es: \n {instructores}")

        instructores.sort()
        print(instructores)
    elif eleccion == 7:
        print("Gracias por usar nuestros servicios.")
        break
    else:
        print("Opcion no valida")
    op=int(input("Digite 1 si desea seguir modificando la lista. \n"
                 "Digite 2 si desea salir. \n"))