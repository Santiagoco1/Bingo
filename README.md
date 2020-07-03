[![Build Status](https://travis-ci.com/Santiagoco1/bingo.svg?branch=master)](https://travis-ci.com/Santiagoco1/bingo)  [![Coverage Status](https://coveralls.io/repos/github/Santiagoco1/bingo/badge.svg?branch=master)](https://coveralls.io/github/Santiagoco1/bingo?branch=master)

# Reglas que hacen que un cartón sea considerado válido:

    1) Los números del carton se encuentran en el rango 1 a 90. 
    2) No hay números repetidos en el carton.
    3) Cada fila de un carton tiene exactamente 5 celdas ocupadas.
    4) Cada carton es una matrix de 3 x 9.
    5) Cada carton tiene 15 celdas ocupadas.
    6) Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
    7) Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
    8) No pueden existir columnas vacias.
    9) No pueden existir columnas con sus tres celdas ocupadas.
    10) Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
    11) En una fila no existen más de dos celdas vacías consecutivas.
    12) En una fila no existen más de dos celdas ocupadas consecutivas.
    13) Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.

Tanto las funciones en el bingo.py como los test, poseen el numero a cual consigna corresponden
