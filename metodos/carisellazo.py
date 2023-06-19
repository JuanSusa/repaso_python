from random import randint
saldo = 50000
#Metodo lanzarMoneda
def lanzarMoneda():
    jugador = input("Digite su nombre: \n")
    print("Bienvenido ", jugador, " al juego de carisellazo")
    moneda = randint(1, 2)
    #print(moneda)
    return moneda
def ganar(saldo, apuesta):
    saldoGana = saldo + apuesta
    print(f"Su saldo es de:  {saldoGana}")

    doblApuesta = input("Desea doblar la apuesta ? s/n\n")
    if doblApuesta == "s":
        saldoGana = apuesta * 2
    else:
        print("Gracias por jugar")
    
def perder(saldo, apuesta):
    saldoPierde= saldo - apuesta
    print(f"Su saldo es de:  {saldoPierde}")
    print("Gracias por jugar")


def jugar():
    moneda = lanzarMoneda()
    
    eleccion=int(input("Digite 1 para Cara y 2 para Sello \n"))
    if eleccion == 1:
        print(f"Usted eligio CARA")
    elif eleccion == 2:
        print(f"Usted eligio SELLO")
    else:
        print("Eleccion Incorrecta")
    apuesta = int(input("Ingrese el valor que desea apostar: \n"))
    confirmacionApuesta = input(f"Seguro que desea apostar ${apuesta} ? s/n\n")
    if confirmacionApuesta == "s":
        print(f"Usted apostó {apuesta}")

        if moneda==1 and eleccion==1:
            print("Felicidades, !ganaste¡ \n" "escogiste Cara y salio Cara")
            ganar(saldo, apuesta)
        elif moneda==1 and eleccion==2:
            print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
            perder(saldo, apuesta)
        elif moneda==2 and eleccion==2:
            print("felicidades, !ganaste¡ \n" "escogiste Sello y salio Sello")
            ganar(saldo, apuesta)
        elif moneda==2 and eleccion==1:
            print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
            perder(saldo, apuesta)
        elif eleccion !=1 and eleccion !=2:
            print("Escogiste un numero incorrecto")
        else:
            print("datos incorrectos")
 
    else:
        print("Eleccion Incorrecta")
    return apuesta

op = True
while True:
    #Invocacion metodos
        print("Bienvenido al juego del CARISELLLAZO")
        jugar()
        op = input("Desea volver a jugar ? s/n")
        if op != True:
            op= False
            print("Gracias por jugar")
        break
    

    




