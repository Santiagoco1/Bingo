#Los ceros representan celdas vacias en el caron.
#Los número uno representan celdas con números en el carton.

def carton():
    mi_carton = (
        (0,1,2,0,4,0,6,0,8),
        (0,0,2,0,4,5,0,0,8),
        (0,1,0,3,4,0,6,7,8)
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