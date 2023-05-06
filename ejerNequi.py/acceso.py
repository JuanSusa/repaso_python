numCelular = 3057847903
password = 9874
saldo = 4500
intentos = 3
op = "s" or "S"


for i in range(1, 4):
    msj = int(input("Ingrese su número de celular\n"))
    psw = int(input("Ingrese su contraseña\n"))

    if msj == numCelular and psw == password:

        while op == "s" or "S":
            print(f"¡Bienvenido a su nequi! \n Su saldo actual es de: {saldo}")
            election = int(input("Qué operación desea realizar el día de hoy:\n"
                              "1. Sacar Dinero\n"
                              "2. Recargar Dinero\n"
                              "3. Transferir Dinero\n"
                              "4. Salir\n"))
            if election == 1:
                select = int(input("Donde desea realizar tu retiro:\n"
                                  "1. Punto Físico\n"
                                  "2. Cajero\n"))
                if select == 1 or select == 2:
                    print(f"Saldo Actual: {saldo}")
                    retiro = int(input("¿Cuantó desea retirar?\n"))
                    if saldo < 2000:
                        print("¡Upps! No te alcanza")
                    elif retiro <= saldo:                        
                        saldo = saldo - retiro
                        print(f"*** Retiro Éxitoso *** \n Su saldo actual es de: {saldo}")
                    else:
                        print("¡Upps! Fondos Insuficientes")
            elif election == 2:
                recarga = int (input("¿Cuantó desea recargar?\n"))
                confirmRecarga = input("Confirme si desea realizar la recarga Si/No\n" )
                if confirmRecarga == "Si" or "si" or "SI":
                    saldo = recarga + saldo
                    print(f"*** Recarga Éxitosa *** \n Su saldo actual es de: {saldo}")
                else:
                    print("*** Gracias por utilizar el servicio ***")
            elif election == 3:                
                select_Transf = int(input("Seleccione a donde desea realizar la transferencia:\n"
                                          "1. A otro nequi\n"
                                          "2. A un banco\n"
                                          "3. TransfiYa"))
                if select_Transf == 1:
                    
                    msj_transf = int (input("Digite el número al que desea realizar la transferencia: \n"))
                    vlr_transfNequi = int(input("Digite el valor a transferir\n"))
                    
                    if vlr_transfNequi <= saldo:
                        saldo = saldo - vlr_transfNequi
                        print(f"*** Transferencia Éxitosa ***\n Su saldo actual es de: {saldo}")
                    else:
                        print("¡Upps! Fondos Insuficientes")
                elif select_Transf == 2:
                    print("*** RECUERDE ***\n" "!A Bancolombia llega de una¡\n" "Si envias LUNES y JUEVES, llega maximo el siguiente día (Si el siguiente día es festivo, llega al dia siguiente hábil)\n" "Si envias el fds verás tu plata en tu netu nequi pero no podras hacer uso de ella")
                    msj_transfBanco = int(input("Seleccione el banco al que desea realizar la transferencia: \n"
                                                "1. Banco BBVA\n"
                                                "2. Banco Bogota\n"
                                                "3. Banco Bancolombia\n"))
                    if msj_transfBanco == 1 or msj_transfBanco == 2:
                        print("Ingresa los datos al del usuario receptor...")
                        tipoCuenta = int(input("Seleccion e tipo de cuenta: \n"
                                               "1. Cuenta de ahorros"
                                               "1. Cuenta corriente"))
                        if tipoCuenta == 1 or tipoCuenta == 2:
                            numCuentaBanco = int (input("Digite el número de cuenta: \n"))
                            vlr_transfNequi = int(input("Digite el valor a transferir\n"))
                            confirmTransBanco = input("Confirme si desea realizar la transferencia Si/No\n" )
                            if confirmTransBanco == "Si" or "si" or "SI":
                                saldo = saldo - vlr_transfNequi
                                print(f"*** Transferencia Éxitosa ***\n Su saldo actual es de: {saldo}")
                            else: 
                                print("*** Gracias por utilizar el servicio ***")
                    elif msj_transfBanco == 3:
                        print("!A Bancolombia llega de una¡")
                        numCuentaBanco = int (input("Digite el número de cuenta: \n"))
                        vlr_transfNequi = int(input("Digite el valor a transferir\n"))
                        confirmTransBanco = input("Confirme si desea realizar la transferencia Si/No\n" )
                        if confirmTransBanco == "Si" or "si" or "SI":
                                saldo = saldo - vlr_transfNequi
                        else: 
                                print("*** Gracias por utilizar el servicio ***")
                    else:
                        print("*** Elección incorrecta ***")
                elif select_Transf == 3:
                    print("*** Envia a otro bancos por TransfiYA ****\n" "Envia dinero a otros bancos con el número del celular. \n Para que tu amig@ reciba la plata, dile que entre a la App de su banco y que acepte el encvio antes de 12Hrs")
                    print("Ingresa los datos al del usuario receptor...")
                    numCelularTransfiYa = int (input("Digite el número de celular TRANSFIYA: \n"))
                    vlr_transfNequi = int(input("Digite el valor a transferir\n"))
                    confirmTransTransfiYA = input("Confirme si desea realizar la transferencia Si/No\n")
                    if confirmTransTransfiYA == "Si" or "si" or "SI":
                            saldo = saldo - vlr_transfNequi
                            print(f"*** Transferencia Éxitosa ***\n Su saldo actual es de: {saldo}")
                    else:
                        print("*** Gracias por utilizar el servicio ***")
            elif election == 4:
                print("Gracias por usar su nequi" )
                break
            else:
                print("*** Elección incorrecta ***")
            
        op = input("Desea continuar con la sesión en su nequi Si o No\n")
        break
    else:
        print("¡Upps! Parece que tus datos de acceso no son correctos, Tienes tres intentos más")
intentos = intentos -1
print("Has gastado los intentos disponibles, tu nequi quedara bloqueado por 2 horas")
