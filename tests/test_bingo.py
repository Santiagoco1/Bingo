
from src.bingo import comprobarCarton
from src.bingo import validar_test_1
from src.bingo import contar_celdas_ocupadas
from src.bingo import validar_test_8
from src.bingo import validar_test_7
from src.bingo import validar_test_6
from src.bingo import validar_una_celda_por_fila
from src.bingo import validar_test_2

carton = comprobarCarton()

def test_validar_1_a_90():
    #Esperemos que cada celda contenga un valor entre 1 y 90
    assert validar_test_1(carton)

def test_validar_celdas_ocupadas():
    #Esperemos contar quince celdas ocupadas
    assert contar_celdas_ocupadas(carton) == 15

def test_validar_celdas_ocupadas_mayor_a_quince():
    #Esperemos contar mas de quince celdas ocupadas
    assert contar_celdas_ocupadas(carton) > 15

def test_validar_celdas_ocupadas_menor_a_quince ():
    #Esperemos contar menos de quince celdas ocupadas
    assert contar_celdas_ocupadas(carton) < 15

def test_validar_una_celda_por_columna():
    #Esperemos que haya una celda por columna
    assert validar_test_8(carton)

def test_validar_orden_creciente_por_columna():
    #Esperemos que haya un orden creciente por columna
    assert validar_test_7(carton)

def test_validar_una_celda_por_fila():
    #Esperemos que haya una celda por fila
    assert validar_una_celda_por_fila(carton)

def test_validar_orden_creciente_fila():
    #Esperemos que haya un orden creciente por fila
    assert validar_test_6(carton)

def test_numeros_repetidos():
    #Esperemos que no haya numeros repetidos
    assert validar_test_2(carton)