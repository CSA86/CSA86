salto_adelante = {4: 75, 5: 15, 19: 41, 28: 50, 35: 96, 44: 82, 53: 94, 59: 95, 70: 91}

salto_atras = {21: 3, 31: 8, 98: 12, 52: 23, 76: 41, 88: 67, 81: 62, 47: 30}

def funcion(combinacion, adelante, atras):
    posicion = 0
    posicion += combinacion[0]
    posicion = saltos(posicion, adelante, atras, False)
    posicion += combinacion[1]
    posicion = saltos(posicion, adelante, atras, False)
    posicion += combinacion[2]
    posicion = saltos(posicion, adelante, atras, False)
    posicion += combinacion[3]
    posicion = saltos(posicion, adelante, atras, False)
    posicion += combinacion[4]
    posicion = saltos(posicion, adelante, atras, False)
    if posicion == 100:
        print(combinacion)
        posicion = 0
        posicion += combinacion[0]
        posicion = saltos(posicion, adelante, atras, True)
        posicion += combinacion[1]
        posicion = saltos(posicion, adelante, atras, True)
        posicion += combinacion[2]
        posicion = saltos(posicion, adelante, atras, True)
        posicion += combinacion[3]
        posicion = saltos(posicion, adelante, atras, True)
        posicion += combinacion[4]
        posicion = saltos(posicion, adelante, atras, True)

def saltos(pos, adelante, atras, eliminar_salto):
    para_eliminar = pos
    if pos in adelante:
        pos = adelante[pos]
        if eliminar_salto:
            print(para_eliminar, '->', pos)
            del adelante[para_eliminar]
    if pos in atras:
        pos = atras[pos]
        if eliminar_salto:
            print(para_eliminar, '->', pos)
            del atras[para_eliminar]
    return pos

import itertools

tiros_de_dado = 5
todas = []
for i in range(tiros_de_dado):
    todas.append([i for i in range(1, 7)])

for combinacion in itertools.product(*todas):
    funcion(combinacion, salto_adelante, salto_atras)
