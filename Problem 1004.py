valido = True

def arma_matriz(fila,columna):
    matriz = []
    lado = []
    for posicion in range(fila):
        matriz.append([0]*columna)
    return matriz

def rigth(una_matriz,posicion_fila,posicion_columna,posicion_final):
    for fila in range(len(una_matriz)):
        if fila == posicion_fila:
            for columna in range(len(una_matriz[fila])):
                if columna >= posicion_columna and columna <= posicion_final:
                    una_matriz[fila][columna] = 1
    return una_matriz

def down(matriz_actual,posicion_fila,posicion_columna,posicion_final):
    for fila in range(len(matriz_actual)):
        if fila >= posicion_fila and fila <= posicion_final:
            for columna in range(len(matriz_actual[fila])):
                if columna == posicion_columna - 1:
                    matriz_actual[fila][columna] = 1
    return matriz_actual

def left(matriz_actual,posicion_fila,posicion_columna,posicion_final):
    for fila in range(len(matriz_actual)):
        if fila == posicion_fila - 1:
            for columna in range(len(matriz_actual[fila])):
                if columna >= posicion_final and columna <= posicion_columna:
                    matriz_actual[fila][columna] = 1
    return matriz_actual

def up(matriz_actual,posicion_fila,posicion_columna,posicion_final):
    for fila in range(len(matriz_actual)):
        if fila <= posicion_fila and fila >= posicion_final:
            for columna in range(len(matriz_actual[fila])):
                if columna == posicion_columna:
                    matriz_actual[fila][columna] = 1
    return matriz_actual


def movimiento_posible(matriz):
    contador = 0
    for fila in matriz:
        if contador > 0:
            break
        else:
            for columna in fila:
                if columna == 0:
                    contador += 1
                    break
    if contador > 0:
        return True
    else:
        return False


while valido:
    print("Entre la cantidad de casos a procesar(solo escriba números en la siguiente línea):")
    try:
        casos_a_procesar = int(input())
        valido = False
    except:
        print('Introduzca un número, no letras por favor:')
for casos in range(casos_a_procesar):
    valido = True
    while valido:
        print('Para el caso', casos, 'introduzca los lados de la matriz a analizar en el orden: filas y columnas')
        lados_de_la_matriz = str(input())
        try:
            filas = int(lados_de_la_matriz.split()[0].strip())
            columnas = int(lados_de_la_matriz.split()[1].strip())
            valido=False
        except:
            print('Por favor introduzca números para la cantidad de filas y columnas, no letras, intente nuevamente')

    matriz_del_juego = arma_matriz(filas,columnas)
    #print(matriz_del_juego)
    movimientos_posibles = True
    derecha_posicion_fila = -1
    derecha_posicion_columna = -1
    derecha_posicion_final = columnas + 1
    abajo_posicion_fila = 0
    abajo_posicion_columna = columnas + 1
    abajo_posicion_final = filas + 1
    izquierda_posicion_fila = filas + 1
    izquierda_posicion_columna = columnas
    izquierda_posicion_final = -1
    arriba_posicion_fila = filas
    arriba_posicion_columna = -1
    arriba_posicion_final = -1
    while movimientos_posibles:
        posicion_del_puntero = 'Derecha'
        derecha_posicion_fila += 1
        derecha_posicion_columna += 1
        derecha_posicion_final -= 1
        resultado_de_movimiento = rigth(matriz_del_juego, derecha_posicion_fila, derecha_posicion_columna, derecha_posicion_final)
        #print('Resultado de derecha:',resultado_de_movimiento)
        movimientos_posibles = movimiento_posible(resultado_de_movimiento)
        if not movimientos_posibles:
            print('El puntero quedó apuntando hacia:', posicion_del_puntero)
            break
        else:
            posicion_del_puntero = 'Abajo'
            abajo_posicion_fila += 1
            abajo_posicion_columna -= 1
            abajo_posicion_final -= 1
            resultado_de_movimiento = down(resultado_de_movimiento, abajo_posicion_fila, abajo_posicion_columna, abajo_posicion_final)
            #print('Resultado de abajo:', resultado_de_movimiento)
            movimientos_posibles = movimiento_posible(resultado_de_movimiento)
            if not movimientos_posibles:
                print('El puntero quedó apuntando hacia:', posicion_del_puntero)
                break
            else:
                posicion_del_puntero = 'Izquierda'
                izquierda_posicion_fila -= 1
                izquierda_posicion_columna -= 1
                izquierda_posicion_final += 1
                resultado_de_movimiento = left(resultado_de_movimiento, izquierda_posicion_fila, izquierda_posicion_columna,izquierda_posicion_final)
                #print('Resultado de izquierda:', resultado_de_movimiento)
                movimientos_posibles = movimiento_posible(resultado_de_movimiento)
                if not movimientos_posibles:
                    print('El puntero quedó apuntando hacia:', posicion_del_puntero)
                    break
                else:
                    posicion_del_puntero = 'Arriba'
                    arriba_posicion_fila -= 1
                    arriba_posicion_columna += 1
                    arriba_posicion_final += 1
                    resultado_de_movimiento = up(resultado_de_movimiento, arriba_posicion_fila,arriba_posicion_columna, arriba_posicion_final)
                    #print('Resultado de arriba:', resultado_de_movimiento)
                    movimientos_posibles = movimiento_posible(resultado_de_movimiento)
                    if not movimientos_posibles:
                        print('El puntero quedó apuntando hacia:', posicion_del_puntero)
                        break
                    else:
                        pass
