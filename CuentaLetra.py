'''Hacer un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase.'''

def CuentaFrase(Frase, Letra):
    cont = 0

    for i in Frase:
        if i == Letra:
            cont += 1

    return cont

Frase = input("Ingresa una frase: ")
Letra = input("Ingresa una letra: ")

contador = CuentaFrase(Frase, Letra)

print("La letra", Letra, "aparece en la frase", Frase, contador, "veces.")