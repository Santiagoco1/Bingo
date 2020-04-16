#Los ceros representan celdas vacias en el caron.
#Los número uno representan celdas con números en el carton.

def carton():
    c = (
        (0,0,0,1,1,0,1,0,1),
        (0,1,0,1,0,1,1,1,1),
        (0,1,0,0,1,0,1,1,0)
    )
    return c

print(carton())