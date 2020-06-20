
from src.generarCarton import intentoCarton

def comprobarCarton():
    for i in range(0, 100000):
        carton = intentoCarton()
        if( validar_test_1(carton) and validar_test_2(carton) and validar_test_3(carton) and validar_test_4(carton) and validar_test_5(carton) and validar_test_6(carton) and validar_test_7(carton) and validar_test_8(carton) and validar_test_9(carton) and validar_test_10(carton) and validar_test_11(carton) and validar_test_12(carton) and validar_test_13(carton)):
            return carton
            break

# Los numeros del carton se encuentran en el rango 1 a 90
def validar_test_1(carton):
    for columna in range(0, 9):
        for celda in range(0, 3):
            if celda != 0:
                if celda < 1 or celda > 90:
                    return False
    return True

# No hay numeros repetidos en el carton.
def validar_test_2(carton):
    ce = 1
    co = 0
    for columna in range(0, 9):
        for celda in range(0, 3):
            if ce == 9:
                ce = 0
                co += 1
            if carton[columna][celda] != 0:
                for columna2 in range(co, 9):
                    for celda2 in range(ce, 3):
                        if carton[columna][celda] == carton[columna2][celda2]:
                            return False
            ce += 1
    return True

# Cada fila de un carton tiene exactamente 5 celdas ocupadas.
def validar_test_3(carton):
    i = 0
    for fila in range(0, 3):
        for columna in range(0, 9):
            if carton[columna][fila] != 0:
                i += 1
        if i != 5:
            return False
        i = 0
    return True

# Cada carton es una matrix de 3 x 9.
def validar_test_4(carton):
    i = 0
    j = 0
    for columna in range(0, 9):
        for fila in range(0, 3):
            i += 1
        if i != 3:
            return False
        i = 0
        j += 1
    if j != 9:
        return False
    return True

# Cada carton tiene 15 celdas ocupadas.
def validar_test_5(carton):
    cont = 0
    for columna in range(0, 9):
        for celda in range(0, 3):
            if carton[columna][celda] != 0:
                cont += 1
    if cont != 15:
        return False
    else:
        return True

# Los numeros de las columnas izquierdas son menores que los de las columnas a la derecha.
def validar_test_6(carton):
    for fila in range(0, 3):
        for columna in range(0, 8):
            if carton[columna][fila] != 0:
                for columna2 in range(columna+1, 9):
                    if carton[columna][fila] >= carton[columna2][fila] and carton[columna2][fila] != 0:
                        return False
    return True

# Para una misma columna, sus numeros estan ordenados de menor a mayor de arriba hacia abajo.
def validar_test_7(carton):
    for columna in range(0, 9):
        for fila in range(0, 2):
            if carton[columna][fila] != 0:
                for fila2 in range(fila+1,3):
                    if carton[columna][fila] >= carton[columna][fila2] and carton[columna][fila2] != 0:
                        return False
    return True

# No pueden existir columnas vacias.
def validar_test_8(carton):
    for columna in range(0, 9):
        cont = 0
        for celda in range(0, 3):
            if carton[columna][celda] == 0:
                cont += 1
        if cont == 3:
            return False
    return True

# No pueden existir columnas con sus tres celdas ocupadas.
def validar_test_9(carton):
    for columna in range(0, 9):
        cont = 0
        for celda in range(0, 3):
            if carton[columna][celda] != 0:
                cont += 1
        if cont == 3:
            return False
    return True

# Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
def validar_test_10(carton):
    contColum = 0
    for columna in range(0, 9):
        contCeldas = 0
        for celda in range(0, 3):
            if carton[columna][celda] == 0:
                contCeldas += 1
        if contCeldas == 2:
            contColum += 1
    if contColum == 3:
        return True
    else:
        return False

# En una fila no existen mas de dos celdas vacias consecutivas.
def validar_test_11(carton):
    for fila in range(0,3):
        for columna in range(0,7):
            if carton[columna][fila] == 0 and carton[columna+1][fila] == 0 and carton[columna+2][fila] == 0:
                return False
    return True 

# En una fila no existen mas de dos celdas ocupadas consecutivas.
def validar_test_12(carton):
    for fila in range(0,3):
        for columna in range(0,7):
            if carton[columna][fila] != 0 and carton[columna+1][fila] != 0 and carton[columna+2][fila] != 0:
                return False
    return True

def validar_test_13(carton):
# Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
    i = 1
    j = 9
    for columna in range(0, 9):
        for fila in range(0, 3):
            if carton[columna][fila] != 0:
                if carton[columna][fila] < i or carton[columna][fila] > j:
                    return False
        if i == 1:
            i += 9
        else:
            i += 10
        if j == 79:
            j += 11
        else:
            j += 10

    return True

comprobarCarton()
