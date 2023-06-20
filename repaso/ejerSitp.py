#Validacion de saldo en la tarjeta
tarSitp = int (input("Acerque su tarjeta para validar su pasaje... \n"))

#Valor pasaje
vlPasaje = 2750
vlTransbordo = 200

saldo_restante = 0


if tarSitp >= vlPasaje:
    saldo_restante = tarSitp - vlPasaje
    msj = "**** bienvenido al sitp ****"
    print(msj.upper()) 
    print("*** Su saldo actual es de: ", saldo_restante, " ***")
    
elif tarSitp < vlPasaje:
        saldo_restante = tarSitp - vlPasaje
        print("**** Su saldo es de: "  , saldo_restante, " ****")
        msj1 = "recuerde recargar su tarjeta antes del proximo uso"
        print(msj1.upper())

eleccTransb = int (input("Desea hacer transbordo \n"
                                "1. Para SI \n"
                                "2. Para NO \n"))
if eleccTransb == 1 and saldo_restante == vlPasaje:
      saldo_restante -= vlTransbordo
      msjTransb = "*** Transferencia exitosa ***"
      print(msjTransb.upper())
      print("**** Su saldo es de: "  , saldo_restante, " ****")
else:
      print("Gracias por viajar con nosotros")
        