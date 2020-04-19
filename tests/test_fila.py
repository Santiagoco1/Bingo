from src.bingo import carton

def test_validar_una_celda_por_fila():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        aux = False
        for i in range(8):
            if( fila[i] == 1):
                aux = True
        if( aux ):
            contador += 1
    if( contador == 3):
        assert True
    else:
        assert False 
    