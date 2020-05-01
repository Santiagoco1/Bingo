#Los ceros representan celdas vacias en el carton.
#Los número uno representan celdas con números en el carton.

def carton():
    mi_carton = (
        (3,0,20,36,0,0,63,71,0),
        (0,13,23,0,42,50,0,75,0),
        (6,0,0,39,0,54,69,0,83)
    )
    return mi_carton

def contar_celdas_ocupadas():
    celdas_vacias = 0
    for fila in carton():
        for celda in fila:
            if celda != 0:
                celdas_vacias += 1

    return celdas_vacias

def validar_una_celda_por_columna ():
    contador_celdas = 0
    for columna in range(0, 9):
        contador = 0
        for fila in carton():
            if fila[columna] != 0:
                contador += 1
        if contador > 0:
            contador_celdas += 1
    return contador_celdas

def validar_1_a_90 ():
    aux = True
    for fila in carton():
        for celda in fila:
            if celda < 1 or celda > 90:
                aux = False
    return aux

def validar_una_celda_por_fila():
    contador_filas = 0
    for fila in carton():
        contador = 0
        for celda in fila:
            if celda > 0: 
                contador += 1
        if contador > 0:
            contador_filas += 1
    return contador_filas

def validar_orden_creciente_filas():
    for fila in carton():
        for i in range(0,8):
            if fila[i] > fila[i+1] and fila[i+1] != 0:
                return False
    return True

def validar_orden_creciente_columnas():
    mi_carton = carton()
    for columna in range(0,9):
        for fila in range(0,2):
            if mi_carton[fila][columna] > mi_carton[fila+1][columna] and mi_carton[fila+1][columna] != 0:
                return False
    return True

def validar_numeros_repetidos():
    c = 1
    f = 0
    mi_carton = carton()
    for fila in carton():
        for celda in fila:
            if c == 9:
                    f += 1
                    c = 0
            if celda != 0:
                for fila2 in range(f,3):
                    for celda2 in range(c,9):
                        if mi_carton[fila2][celda2] == celda:
                            return False
            c += 1
    return True


