
from src.bingo import comprobarCarton
from src.bingo import validar_test_1
from src.bingo import validar_test_2
from src.bingo import validar_test_3
from src.bingo import validar_test_4
from src.bingo import validar_test_5
from src.bingo import validar_test_6
from src.bingo import validar_test_7
from src.bingo import validar_test_8
from src.bingo import validar_test_9
from src.bingo import validar_test_10
from src.bingo import validar_test_11
from src.bingo import validar_test_12
from src.bingo import validar_test_13


carton = comprobarCarton()

def test_1():
    # Los numeros del carton se encuentran en el rango 1 a 90
    assert validar_test_1(carton)

def test_2():
    # No hay numeros repetidos en el carton.
    assert validar_test_2(carton)

def test_3():
    # Cada fila de un carton tiene exactamente 5 celdas ocupadas.
    assert validar_test_3(carton)

def test_4():
    # Cada carton es una matrix de 3 x 9.
    assert validar_test_4(carton)

def test_5():
    # Cada carton tiene 15 celdas ocupadas.
    assert validar_test_5(carton)

def test_6():
    # Los numeros de las columnas izquierdas son menores que los de las columnas a la derecha.
    assert validar_test_6(carton)

def test_7():
    # Para una misma columna, sus numeros estan ordenados de menor a mayor de arriba hacia abajo.
    assert validar_test_7(carton)

def test_8():
    # No pueden existir columnas vacias.
    assert validar_test_8(carton)

def test_9():
    # No pueden existir columnas con sus tres celdas ocupadas.
    assert validar_test_9(carton)

def test_10():
    # Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
    assert validar_test_10(carton)

def test_11():
    # En una fila no existen mas de dos celdas vacias consecutivas.
    assert validar_test_11(carton)

def test_12():
    # En una fila no existen mas de dos celdas ocupadas consecutivas.
    assert validar_test_12(carton)

def test_13():
    # Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
    assert validar_test_13(carton)