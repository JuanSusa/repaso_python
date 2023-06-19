#Declaracion de un metodo
def sumar (n1, n2):
    #Cuerpo del metodo
    print ("Es un metodo de Suma")
    suma = n1 + n2
    return suma


#metod con parametros
def resta(n1, n2):
    restar = n1 - n2
    print(f"La resta entre {n1} y  {n2}  es de:  {restar}")

#metodo con un valor de retorno
def multiplicacion(n1, n2):
    #Cuerpo del metodo
    multiplicar = n1 * n2
    #Retorno del valor
    return multiplicar



#Llamado o invocacion del metodo 
print("Menú de opciones")
op = int(input("Ingrese la opcion según la operación a realizar \n 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. División\n 5. Promedio\n"))

num1 = int(input("Ingrese el numero 1: \n"))
num2 = int(input("Ingrese el numero 2: \n"))
Numeros = [num1,num2]

if op == 1:
    #Invocacion metodo suma 
    sumar()

elif op == 2:
    #Invocacion metodo con parametros
    resta(num1, num2)

elif op == 3:
    #Invocacion metodo con retorno
    #multiplicaion(num1, num2)
    
    #Valor de retorno directamente en una impresion
    print(f"El resultado entre {num1} y {num2} es de: {multiplicacion(num1, num2)}")

    #Guardar en una variable para utilizarlo en otro momento
    producto = multiplicacion(num1, num2)
    if producto < 50:
        print("El resultado de la multiplicaion es menor de 50")
    else:
        print("El resultado de la multiplicaion es mayor de 50")

elif op == 5:
    resultadoSuma = sumar(num1, num2)
    cantidadNum = len (Numeros)
    print(f"El resultado de la suma es de: {resultadoSuma}")
    promedio = resultadoSuma / cantidadNum
    print(f"El resultado del promedio es de: {promedio}")
    




