"""Un profesor de matemática necesita generar la tabla 
de multiplicar de un número entero comprendido entre 1 y 10. """

numero = int(input("Por favor ingrese el numero de la tabla que quiere generar: "))

mult = 1


while mult <= 10 :

    res = numero * mult
    
    print(f"{numero} x {mult} = {res}")

    mult += 1

