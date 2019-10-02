def iteracion1(cadena):
    if cadena== "":
        return [0]
    elif "," in cadena:
        numeros = cadena.split(",")
        cantidad = 0
        for num in numeros:
            cantidad +=1
        return [cantidad]
    else:
        return [1]

def iteracion2(cadena):
    return [0,0]


class KataSimple:
    pass
