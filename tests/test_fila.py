from src.bingo import validar_una_celda_por_fila

def test_validar_una_celda_por_fila():
    #Esperemos que haya una celda por fila
    assert validar_una_celda_por_fila() == 3