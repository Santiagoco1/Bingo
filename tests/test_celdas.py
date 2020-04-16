from src.bingo import carton

def contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    
    # Esoeramos encontrar 15 celdas ocupadas.
    return contador

def test_validar_celdas_ocupadas_igual_a_quince():
    assert contar_celdas_ocupadas() == 15

def test_validar_celdas_ocupadas_mayor_a_quince ():
    assert contar_celdas_ocupadas() > 15

def test_validar_celdas_ocupadas_menor_a_quince ():
    assert contar_celdas_ocupadas() < 15

def test_validar_una_celda_por_columna():
    contador = 0
    celda_columna = True
    mi_carton = carton()
    for i in range(8):
        for fila in mi_carton:
            contador += fila[i]
        if contador < 1:
            celda_columna = False

    assert celda_columna