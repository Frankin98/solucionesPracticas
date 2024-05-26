"""Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando los recursos 
ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:
Mostrar al usuario un menú de opciones
Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe agregar al diccionario a la persona que el usuario ingrese
Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera.
Opción 3: Eliminar una persona del diccionario. Elimina según el DNI
Opción 4: Mostrar todos la agenda
Opción 5: Salir"""


diccionario = {}

print("************************************")
print("*Bienvenido a su agenda telefonica.*")

while True :

    print("************************************")
    print("Opción 1: Agregar una persona.")
    print("Opción 2: Modificar una persona.")
    print("Opción 3: Eliminar una persona del diccionario.")
    print("Opción 4: Mostrar todos la agenda")
    print("Opción 5: Salir")


    opcion = int(input("Por favor seleccione una opcion: "))

    if opcion == 1:
        print ("Por favor ingrese los siguientes datos de su nuevo contacto: ")
        apellido = input("Apellido: ").capitalize()
        nombre = input("Nombre: ").capitalize()
        dni = int(input("DNI: "))
        email= input("Email: ")
        celular = int(input("Número de telefono: "))
        diccionario[dni] = {"Apellido": apellido, "Nombre": nombre,"Email": email, "Número de telefono": celular}
        print ("El contacto se agrego correctamente.")
        

    elif opcion == 2:
        modificar_dni = int(input("Por favor ingrese el DNI del contacto a modificar: "))

        if modificar_dni in diccionario:
            print("¿Que desea modificar?")
            print ("1) Apellido")
            print ("2) Nombre")
            print ("3) Email")
            print ("4) Número de telefono")
            modificar = int(input("Por favor indique con número: "))

            if modificar == 1:
                ape_nuev = input("Por favor ingrese nuevo apellido: ")
                diccionario[modificar_dni]["Apellido"] = ape_nuev
                print ("Se ha modificado con éxito el apellido.") 

            elif modificar == 2:
                nom_nuev = input("Por favor ingrese nuevo nombre: ")
                diccionario[modificar_dni]["Nombre"] = nom_nuev
                print ("Se ha modificado con éxito el nombre.")

            elif modificar == 3:
                ema_nuev = input("Por favor ingrese nuevo email: ")
                diccionario[modificar_dni]["Email"] = ema_nuev
                print ("Se ha modificado con éxito el email.")
            
            elif modificar == 4:
                cel_nuev = int(input("Por favor ingrese nuevo número de telefono: "))
                diccionario[modificar_dni]["Número de telefono"] = cel_nuev
                print ("Se ha modificado con éxito el número de telefono.")
                True
        else:
            print("El DNI no está agendado.")


    elif opcion == 3:

        eliminar_dni = int(input("Por favor ingrese el DNI de contacto que quiere eliminar: "))

        if eliminar_dni in diccionario:
            confirmar = int(input("Para confirmar presione 1, para cancelar 2. "))

            if confirmar == 1 :
                del diccionario[eliminar_dni]
                print("El contacto se ha eliminado con éxito.")
                
            else:
                print("Se canceló la acción.")
            
            
    elif opcion == 4:
        print(diccionario)
        True

    elif opcion == 5:
        print("Saliendo de la agenda.")
        break
    else:
        print("************************************")
        print("La opcion ingresada no es valida.")
        print("Por favor intente nuevamente")
        