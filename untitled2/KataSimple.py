def iteracion1(cadena):
    if cadena == "":
        return [0]
    elif "," in cadena:
        numeros = cadena.split(",")
        cantidad = 0
        for num in numeros:
            cantidad += 1
        return [cantidad]
    else:
        return [1]


def iteracion2(cadena):
    if cadena == "":
        return [0, 0]
    elif "," in cadena:
        numeros = cadena.split(",")
        cantidad = 0
        for num in numeros:
            cantidad += 1

        return [cantidad, int(min(numeros))]
    else:
        return [1, int(min(cadena))]


def iteracion3(cadena):
    if cadena == "":
        return [0, 0, 0]
    elif "," in cadena:
        numeros = cadena.split(",")
        cantidad = 0
        for num in numeros:
            cantidad += 1

        return [cantidad, int(min(numeros)),int(max(numeros))]
    else:
        return [1, int(min(cadena)),int(max(cadena))]


def iteracion4(cadena):
    if cadena == "":
        return [0, 0, 0,0]
    elif "," in cadena:
        numeros = cadena.split(",")
        cantidad = 0
        suma = 0
        for num in numeros:
            cantidad += 1
            suma = int(num)+suma

        return [cantidad, int(min(numeros)), int(max(numeros)),suma/cantidad]
    else:
        return [1, int(min(cadena)), int(max(cadena)), 1]


class KataSimple:
    pass
