from src.bingo import contar_celdas_ocupadas
from src.bingo import validar_una_celda_por_columna

def test_validar_celdas_ocupadas():
    #Esperemos contar quince celdas ocupadas
    assert contar_celdas_ocupadas() == 15

def test_validar_celdas_ocupadas_mayor_a_quince ():
    #Esperemos contar mas de quince celdas ocupadas
    assert contar_celdas_ocupadas() > 15

def test_validar_celdas_ocupadas_menor_a_quince ():
    #Esperemos contar menos de quince celdas ocupadas
    assert contar_celdas_ocupadas() < 15

def test_validar_una_celda_por_columna():
    #Esperemos que haya una celda por columna
    assert validar_una_celda_por_columna() == 9
    