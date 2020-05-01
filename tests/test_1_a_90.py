from src.bingo import validar_1_a_90

def test_validar_uno_a_noventa():
    #Esperemos que cada celda contenga un valor entre 1 y 90
    assert validar_1_a_90()