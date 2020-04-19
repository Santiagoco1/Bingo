#Los ceros representan celdas vacias en el caron.
#Los número uno representan celdas con números en el carton.

def carton():
    mi_carton = (
        (0,0,0,0,0,0,0,0,0),
        (0,1,0,1,0,1,1,1,1),
        (0,1,0,0,1,0,1,1,0)
    )
    return mi_carton

def columna(carton, nro_columna):
    return (
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna]
    )

print(columna(carton(), 1))