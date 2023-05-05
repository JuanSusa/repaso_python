"""
#Preguntar tipo de gasolina: corriente (10800)
#Solicitar valor a tanquear
#Mostrar cuantos galones se tanquearon
#Ejercicio practica 1
valor = int (input("ingrese el valor que desea tanquear: \n"))
prGalon = 10800
tanqueada = valor / prGalon
print("Usted a tanqueado ", tanqueada, " galon(es) \n Gracias por su compra")
"""
#Preguntar tipo de gasolina: corriente (10800), disiel (9800)
#Solicitar valor a tanquear
#Mostrar cuantos galones se tanquearon

prCorriente = 10800
prDisiel = 9800
tipComb = int (input("Seleccione que tipo de combustible desea tanquear \n"
                     "1. Gasolina Corriente \n"
                     "2. Gasolina Disiel \n"))
if tipComb == 1:
    valorComb = int (input("Ingrese el valor que desea tanquear: \n"))
    totalTanqueada = valorComb / prCorriente
    print("Usted a tanqueado ", totalTanqueada, " galon(es) \n Gracias por su compra")
elif tipComb == 2:
    valorComb = int (input("Ingrese el valor que desea tanquear: \n"))
    totalTanqueada = valorComb /prDisiel
    print("Usted a tanqueado ", totalTanqueada, " galon(es) \n Gracias por su compra")
else:
    print("Seleccion invalida")  




# elif tarSitp < vlPasaje:
#     msjError = "saldo insuficiente \n Por favor recargue su tarjeta"
#     print(msjError.upper())