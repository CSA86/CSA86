
def matriz_juego():
    matriz=[]
    for i in range(3):
        a=['_']*3
        matriz.append(a)
    return matriz

def tablero():
    tabla=[]
    for i in range(3):
        a=[0]*5
        tabla.append(a)
    for a in range(3):
        for b in range(5):
            if a==0 or a==1:
                if b==0 or b==2 or b==4:
                    tabla[a][b]='_'
                else:
                    tabla[a][b]='|'
            else:
                if b==0 or b==2 or b==4:
                    tabla[a][b]=' '
                else:
                    tabla[a][b]='|'
    return tabla

def imprime_matriz(matriz):
    fila=''
    for a in range(3):
        fila = ''
        for b in range(5):
            fila+=str(matriz[a][b])
        print(fila)
    return

def actualiza_matriz_tablero_desde_matriz_posiciones(posiciones,tablero):
    for a in range(3):
        for b in range(3):
            if a<2:
                if b==0:
                    tablero[a][b]=posiciones[a][b]
                elif b==1:
                    tablero[a][2]=posiciones[a][b]
                else:
                    tablero[a][4] = posiciones[a][b]
            else:
                if b==0:
                    if posiciones[a][b]!='_':
                        tablero[a][b]=posiciones[a][b]
                    else:
                        tablero[a][b]=' '
                elif b==1:
                    if posiciones[a][b]!='_':
                        tablero[a][2]=posiciones[a][b]
                    else:
                        tablero[a][2]=' '
                else:
                    if posiciones[a][b]!='_':
                        tablero[a][4]=posiciones[a][b]
                    else:
                        tablero[a][4]=' '

def asigna_valores_a_matriz_posiciones(posiciones,row,column,quien_juega):
    for a in range(3):
        for b in range(3):
            if a==row and b==column:
                if quien_juega=='X':
                    posiciones[a][b]='X'
                else:
                    posiciones[a][b] = 'O'
    return posiciones

def busca_movida_final(posiciones):
    movida_final=''
    for a in range(3):
        for b in range(3):
            if posiciones[a][b] == '_':
                proxima_movida_fila = a
                proxima_movida_columna = b
    movida_final=str(proxima_movida_fila)+str(proxima_movida_columna)
    return movida_final

def verifica_movimiento_ganador(posiciones):
    movida_ganadora=''
    for a in range(3):
        x_en_fila=0
        vacias_fila=0
        for b in range(3):
            if posiciones[a][b]=='X':
               x_en_fila+=1
            if posiciones[a][b]=='_':
                vacias_fila+=1
                proxima_movida_fila=a
                proxima_movida_columna=b
            if b==2:
                if x_en_fila==2 and vacias_fila==1:
                    movida_ganadora=str(proxima_movida_fila)+str(proxima_movida_columna)
    for c in range(3):
        x_en_columna=0
        vacias_columna=0
        for d in range(3):
            if posiciones[d][c]=='X':
               x_en_columna+=1
            if posiciones[d][c]=='_':
                vacias_columna+=1
                proxima_movida_fila=d
                proxima_movida_columna=c
            if d==2:
                if x_en_columna==2 and vacias_columna==1:
                    movida_ganadora = str(proxima_movida_fila) + str(proxima_movida_columna)
    x_en_diagonal_derecha = 0
    vacias_diagonal_derecha = 0
    for e in range(3):
        for f in range(3):
            if e==0 and f==0 and posiciones[e][f]=='X':
                x_en_diagonal_derecha+=1
            if e==1 and f==1 and posiciones[e][f]=='X':
                x_en_diagonal_derecha += 1
            if e==2 and f==2 and posiciones[e][f]=='X':
                x_en_diagonal_derecha += 1
            if e == 0 and f == 0 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 1 and f == 1 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 2 and f == 2 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
    if x_en_diagonal_derecha==2 and vacias_diagonal_derecha==1:
        movida_ganadora = str(proxima_movida_fila) + str(proxima_movida_columna)
    x_en_diagonal_izquierda = 0
    vacias_diagonal_izquierda = 0
    for g in range(3):
        for h in range(3):
            if g==0 and h==2 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda+=1
            if g==1 and h==1 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda += 1
            if g==2 and h==0 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda += 1
            if g == 0 and h == 2 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda+=1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 1 and h == 1 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 2 and h == 0 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
    if x_en_diagonal_izquierda==2 and vacias_diagonal_izquierda==1:
        movida_ganadora = str(proxima_movida_fila) + str(proxima_movida_columna)
    return movida_ganadora

def evita_movimiento_ganador_del_contrario(posiciones):
    movida_que_salva=''
    for a in range(3):
        x_en_fila=0
        vacias_fila=0
        for b in range(3):
            if posiciones[a][b]=='O':
               x_en_fila+=1
            if posiciones[a][b]=='_':
                vacias_fila+=1
                proxima_movida_fila=a
                proxima_movida_columna=b
            if b==2:
                if x_en_fila==2 and vacias_fila==1:
                    movida_que_salva=str(proxima_movida_fila)+str(proxima_movida_columna)
    for c in range(3):
        x_en_columna=0
        vacias_columna=0
        for d in range(3):
            if posiciones[d][c]=='O':
               x_en_columna+=1
            if posiciones[d][c]=='_':
                vacias_columna+=1
                proxima_movida_fila=d
                proxima_movida_columna=c
            if d==2:
                if x_en_columna==2 and vacias_columna==1:
                    movida_que_salva = str(proxima_movida_fila) + str(proxima_movida_columna)
    x_en_diagonal_derecha = 0
    vacias_diagonal_derecha = 0
    for e in range(3):
        for f in range(3):
            if e==0 and f==0 and posiciones[e][f]=='O':
                x_en_diagonal_derecha+=1
            if e==1 and f==1 and posiciones[e][f]=='O':
                x_en_diagonal_derecha += 1
            if e==2 and f==2 and posiciones[e][f]=='O':
                x_en_diagonal_derecha += 1
            if e == 0 and f == 0 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 1 and f == 1 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 2 and f == 2 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
    if x_en_diagonal_derecha==2 and vacias_diagonal_derecha==1:
        movida_que_salva = str(proxima_movida_fila) + str(proxima_movida_columna)
    x_en_diagonal_izquierda = 0
    vacias_diagonal_izquierda = 0
    for g in range(3):
        for h in range(3):
            if g==0 and h==2 and posiciones[g][h]=='O':
                x_en_diagonal_izquierda+=1
            if g==1 and h==1 and posiciones[g][h]=='O':
                x_en_diagonal_izquierda += 1
            if g==2 and h==0 and posiciones[g][h]=='O':
                x_en_diagonal_izquierda += 1
            if g == 0 and h == 2 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda+=1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 1 and h == 1 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 2 and h == 0 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
    if x_en_diagonal_izquierda==2 and vacias_diagonal_izquierda==1:
        movida_que_salva = str(proxima_movida_fila) + str(proxima_movida_columna)
    return movida_que_salva

def estrategia_de_continuacion_del_juego(posiciones):
    movida_tactica_columna=[]
    movida_tactica_fila=[]
    movida_tactica_diagonal_derecha=''
    movida_tactica_diagonal_izquierda=''
    for a in range(3):
        temporal = []
        x_en_fila=0
        vacias_fila=0
        for b in range(3):
            if posiciones[a][b]=='X':
               x_en_fila+=1
            if posiciones[a][b]=='_':
                vacias_fila+=1
                proxima_movida_fila=a
                proxima_movida_columna=b
                temporal.append(str(proxima_movida_fila) + str(proxima_movida_columna))
            if b==2:
                #print('Final de la fila:',a,'x en fila:',x_en_fila,'vacia en fila:',vacias_fila)
                if x_en_fila==1 and vacias_fila==2:
                    movida_tactica_fila.append(temporal)
    for c in range(3):
        temporal = []
        x_en_columna=0
        vacias_columna=0
        for d in range(3):
            if posiciones[d][c]=='X':
               x_en_columna+=1
            if posiciones[d][c]=='_':
                vacias_columna+=1
                proxima_movida_fila=d
                proxima_movida_columna=c
                temporal.append(str(proxima_movida_fila) + str(proxima_movida_columna))
            if d==2:
                #print('Final de la columna:', c, 'x en columna:', x_en_columna, 'vacia en columna:', vacias_columna)
                if x_en_columna==1 and vacias_columna==2:
                    movida_tactica_columna.append(temporal)
    x_en_diagonal_derecha = 0
    vacias_diagonal_derecha = 0
    for e in range(3):
        for f in range(3):
            if e==0 and f==0 and posiciones[e][f]=='X':
                x_en_diagonal_derecha+=1
            if e==1 and f==1 and posiciones[e][f]=='X':
                x_en_diagonal_derecha+=1
            if e==2 and f==2 and posiciones[e][f]=='X':
                x_en_diagonal_derecha+=1
            if e == 0 and f == 0 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 1 and f == 1 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
            if e == 2 and f == 2 and posiciones[e][f] == '_':
                vacias_diagonal_derecha+=1
                proxima_movida_fila = e
                proxima_movida_columna = f
    if x_en_diagonal_derecha==1 and vacias_diagonal_derecha==2:
        movida_tactica_diagonal_derecha = str(proxima_movida_fila) + str(proxima_movida_columna)
    x_en_diagonal_izquierda = 0
    vacias_diagonal_izquierda = 0
    for g in range(3):
        for h in range(3):
            if g==0 and h==2 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda+=1
            if g==1 and h==1 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda += 1
            if g==2 and h==0 and posiciones[g][h]=='X':
                x_en_diagonal_izquierda += 1
            if g == 0 and h == 2 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda+=1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 1 and h == 1 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
            if g == 2 and h == 0 and posiciones[g][h] == '_':
                vacias_diagonal_izquierda += 1
                proxima_movida_fila = g
                proxima_movida_columna = h
    if x_en_diagonal_izquierda==1 and vacias_diagonal_izquierda==2:
        movida_tactica_diagonal_izquierda = str(proxima_movida_fila) + str(proxima_movida_columna)
    #print('Esto es dentro de la funcion estrategia...,movida tactica fila:',movida_tactica_fila,'movida tactica columna',movida_tactica_columna,'movida tactica diag der',movida_tactica_diagonal_derecha,'movida tact diag izq', movida_tactica_diagonal_izquierda)
    if movida_tactica_fila and movida_tactica_columna:
        movida_que_lleva_a_la_victoria=''
        for orden_fila,posicion_fila in enumerate(movida_tactica_fila[0]):
            for posicion_columna in movida_tactica_columna[0]:
                if posicion_fila==posicion_columna:
                    movida_que_lleva_a_la_victoria=str(movida_tactica_fila[0][orden_fila])
                    #print('Esta movida garantiza la victoria:',movida_que_lleva_a_la_victoria)
                    return movida_que_lleva_a_la_victoria
    elif not movida_tactica_fila and movida_tactica_columna:
        #print('movida tactica en columna')
        return str(movida_tactica_columna[0][0])
    elif movida_tactica_fila and not movida_tactica_columna:
        #print('movida tactica en fila')
        return str(movida_tactica_fila[0][0])
    else:
        if movida_tactica_diagonal_derecha:
            #print('movida tactica diagonal derecha')
            return str(movida_tactica_diagonal_derecha)
        else:
            #print('movida tactica diagonal izquierda')
            return str(movida_tactica_diagonal_izquierda)

print('En cada movimiento especifique la posicion donde desea ubicar su jugada señalando fila y columna con un par de numeros separados por un guion medio, Ejemplo: 1-3 para la posicion fila 1 columna 3')
no_fin_del_juego=True
while no_fin_del_juego:
    for turno in range(9):
        if turno==0:
            posiciones_ocupadas = []
            matriz_posiciones = matriz_juego()
            matriz_tablero = tablero()
            matriz_posiciones[1][1] = 'X'
            posiciones_ocupadas.append('2-2')
            actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
            print('La PC hace su movida:')
            imprime_matriz(matriz_tablero)
        elif turno==2:
            movimiento ='X'
            #print(movida_usuario)
            if movida_usuario=='1-1' or movida_usuario=='1-3':
                matriz_posiciones[0][1] = 'X'
                posiciones_ocupadas.append('1-2')
                #print('Este juego termina en tablas')
            elif movida_usuario=='3-1' or movida_usuario=='3-3':
                matriz_posiciones[2][1] = 'X'
                posiciones_ocupadas.append('3-2')
                #print('Este juego termina en tablas')
            elif movida_usuario=='1-2' or movida_usuario=='2-1':
                matriz_posiciones[0][0] = 'X'
                posiciones_ocupadas.append('1-1')
                #print('En este juego gana la PC')
            else:
                matriz_posiciones[2][2] = 'X'
                posiciones_ocupadas.append('3-3')
                #print('En este juego gana la PC')
            actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
            print('La PC hace su movida:')
            imprime_matriz(matriz_tablero)
        elif turno==4 or turno==6:
            movimiento ='X'
            movida_ganadora=verifica_movimiento_ganador(matriz_posiciones)
            if movida_ganadora:
                fila=int(movida_ganadora[0])
                columna=int(movida_ganadora[1])
                asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                print('La PC hace su movida:')
                imprime_matriz(matriz_tablero)
                print('********GAME OVER********')
                print('Desea volver a jugar, diga si ó no:')
                continuacion = input()
                #print(continuacion)
                if continuacion == 'n' or continuacion == 'N' or continuacion == 'no' or continuacion == 'No' or continuacion == 'NO':
                    no_fin_del_juego = False
                    break
                else:
                    no_fin_del_juego = True
                    break
                    #print(no_fin_del_juego)
            else:
                movida_salvadora=evita_movimiento_ganador_del_contrario(matriz_posiciones)
                if movida_salvadora:
                    fila = int(movida_salvadora[0])
                    columna = int(movida_salvadora[1])
                    asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                    actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                    print('La PC hace su movida:')
                    imprime_matriz(matriz_tablero)
                else:
                    movida_tactica=estrategia_de_continuacion_del_juego(matriz_posiciones)
                    #print('Movida tactica',movida_tactica)
                    fila=int(movida_tactica[0])
                    columna=int(movida_tactica[1])
                    #print(matriz_posiciones,fila,columna,movimiento)
                    asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                    actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                    print('La PC hace su movida:')
                    imprime_matriz(matriz_tablero)
        elif turno==8:
            movimiento = 'X'
            movida_ganadora = verifica_movimiento_ganador(matriz_posiciones)
            if movida_ganadora:
                fila = int(movida_ganadora[0])
                columna = int(movida_ganadora[1])
                asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                print('La PC hace su movida:')
                imprime_matriz(matriz_tablero)
                print('********GAME OVER********')
            else:
                movida_salvadora = evita_movimiento_ganador_del_contrario(matriz_posiciones)
                if movida_salvadora:
                    fila = int(movida_salvadora[0])
                    columna = int(movida_salvadora[1])
                    asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                    actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                    print('La PC hace su movida:')
                    imprime_matriz(matriz_tablero)
                else:
                    movimiento = 'X'
                    movida_final=busca_movida_final(matriz_posiciones)
                    fila=int(movida_final[0])
                    columna=int(movida_final[1])
                    asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
                    actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
                    print('La PC hace su movida:')
                    imprime_matriz(matriz_tablero)
                    print('TABLAS')
            print('Desea volver a jugar, diga si ó no:')
            continuacion=input()
            print(continuacion)
            if continuacion=='n' or continuacion=='N' or continuacion=='no' or continuacion=='No' or continuacion=='NO' :
                no_fin_del_juego=False
            else:
                no_fin_del_juego = True
                print(no_fin_del_juego)
        else:
            movimiento = 'O'
            valido = True
            while valido:
                print('Introduzca su movida')
                movida_usuario = str(input())
                if len(movida_usuario) < 3:
                    print('Le faltan datos por introducir')
                elif len(movida_usuario) > 3:
                    print('Ha introducido demasiados datos')
                else:
                    if '-' in movida_usuario:
                        try:
                            fila = int(movida_usuario.split('-')[0].strip()) - 1
                            columna = int(movida_usuario.split('-')[1].strip()) - 1
                            if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2:
                                if movida_usuario not in posiciones_ocupadas:
                                    valido = False
                                    posiciones_ocupadas.append(movida_usuario)
                                else:
                                    print('Por favor introduzca una posición que no esté ocupada')
                            else:
                                print('Por favor, introduzca números entre 1 y 3')
                        except:
                            print('Por favor introduzca números, no letras, intente nuevamente')
                    elif '-' not in movida_usuario:
                        print('Separe el orden de fila y columna con un guion medio: -')
            asigna_valores_a_matriz_posiciones(matriz_posiciones, fila, columna, movimiento)
            actualiza_matriz_tablero_desde_matriz_posiciones(matriz_posiciones, matriz_tablero)
            imprime_matriz(matriz_tablero)