'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla
si es mayor de edad,
si es menor de edad o si es adulto mayor 65 y más'''


#Edaad
salir = False

while not salir:
    Edad = int(input("Qué edad tienes? "))
    if Edad > 0:
        if Edad < 18:
            print("Eres menor de edad")
        elif Edad >= 18 and Edad < 60:
            print("Eres mayor de edad")
        elif Edad >= 60 and Edad < 90:
            print("Ya puedes solicitar la tarjeta del cabezita de algodón")
        else:
            print("Ya estas viejito...")
    else:
        salir = True











