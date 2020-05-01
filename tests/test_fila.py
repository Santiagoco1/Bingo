from src.bingo import validar_una_celda_por_fila
from src.bingo import validar_orden_creciente_filas

def test_validar_una_celda_por_fila():
    #Esperemos que haya una celda por fila
    assert validar_una_celda_por_fila() == 3

def test_validar_orden_creciente_fila():
    #Esperemos que haya un orden creciente por fila
    assert validar_orden_creciente_filas()