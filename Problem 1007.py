import operator

def recorrido_cuadrado(matriz,fila,columna,numero,umbral):
    resultado = 0
    for poscion, valor in enumerate(matriz[fila:fila+numero]):
        for posicion1, valor1 in enumerate(valor[columna:columna+numero]):
            resultado += int(valor1)
    if resultado <= int(umbral):
        return resultado
    else:
        return False

valido = True
while valido:
    print("Entre la cantidad de casos a procesar(solo escriba números en la siguiente línea):")
    try:
        casos_a_procesar = int(input())
        valido = False
    except:
        print('Introduzca un número, no letras por favor:')
for casos in range(casos_a_procesar):
    valido = True
    cuadrado = []
    while valido:
        print('Para el caso', casos, 'introduzca la cantidad de bloques por cada lado de la ciudad')
        try:
            lado_del_cuadrado = int(input())
            valido = False
        except:
            print('Por favor introduzca un número, no letras, intente nuevamente')
    matriz_consumo = []
    print('Introduzca la cantidad de consumidores por cada bloque, respete la cantidad de bloques por lado')
    for fila in range(lado_del_cuadrado):
        valido=False
        while not valido:
            datos_fila = str(input())
            variable = datos_fila.split()
            if len(variable) != lado_del_cuadrado:
                print('Los datos introducidos no coinciden con la cantidad de bloques por fila')
            else:
                for a in range(lado_del_cuadrado):
                    try:
                        valido = int(variable[a])
                    except:
                        print('Para la posición',a,'de esta fila, introduzca números, no otro tipo de caracter por favor, intente nuevamente')
                        valido = False
        matriz_consumo.append(variable)
    dato_introducido = True
    print('A continuación introduzca en cada línea los requerimientos de cada proyecto, lo cual consiste en la cantidad de consumidores que deben ser cubiertos, cuando no haya más proyectos que incluir introduzca un 0 (cero)')
    requerimiento_de_proyecto = []
    while dato_introducido:
        valido = False
        while not valido:
            requerimiento = str(input())
            var = requerimiento.split()[0]
            try:
                valido = int(var[0])
                if int(var[0]) > 0:
                    requerimiento_de_proyecto.append(var)
                else:
                    dato_introducido = False
                    break
            except:
                print('Introduzca números, no letras por favor')
    #print(matriz_consumo)
    #print(requerimiento_de_proyecto)

    for proyecto in requerimiento_de_proyecto:
        print(proyecto)
        consumidores_ciudad = 0
        posicion_consumidores_cubiertos = {}
        posicion_lado_del_bloque = {}
        for orden, fila1 in enumerate(matriz_consumo):
            for orden1, columna in enumerate(fila1):
                lugar = str(orden)+str(orden1)
                consumidores_ciudad += int(columna)
                #print(lugar)
                for n in range(1,len(matriz_consumo)):
                    if n <= len(matriz_consumo)-orden and n <= len(matriz_consumo)-orden1:
                        resultado_de_funcion = recorrido_cuadrado(matriz_consumo, orden, orden1, n, proyecto)
                        if resultado_de_funcion:
                            posicion_consumidores_cubiertos.update({lugar: resultado_de_funcion})
                            posicion_lado_del_bloque.update({lugar: n})
        #print(posicion_consumidores_cubiertos)
        #print(posicion_lado_del_bloque)
        resultado = sorted(posicion_consumidores_cubiertos.items(), key=operator.itemgetter(1))
        resultado.reverse()
        #print(resultado)
        solucion = {}
        cambia = False
        for orden,respuestas in enumerate(resultado):
            if orden == 0:
                solucion.update({respuestas[0]: respuestas[1]})
            if orden > 0:
                for valor in solucion.values():
                    if int(respuestas[1]) == int(valor):
                        cambia = True
                    else:
                        cambia = False
            if cambia:
                solucion.update({respuestas[0]: respuestas[1]})
        #print(solucion)
        #print(len(solucion))
        if len(solucion) == 1:
            for clave, valor in solucion.items():
                for clave1, valor1 in posicion_lado_del_bloque.items():
                    if clave == clave1:
                        print('City: New York')
                        print('Power Supplied:', valor,'consumer(s)')
                        print('Covered Area:', valor1,' X ', valor1,'block(s)')
                        print('Power Deficit:', consumidores_ciudad-int(valor), 'consumer(s)')
                        print('Ubicación dentro de la matriz de la primera posición del bloque escogido(contando de arriba hacia abajo de izquierda a derecha):',clave)
        else:
            respuesta_final = 0
            for clave2, valor2 in solucion.items():
                for clave3, valor3 in posicion_lado_del_bloque.items():
                    if clave2 == clave3:
                        if int(valor3) > int(respuesta_final):
                            respuesta_final = valor3
                            posicion = clave3
            for clave4, valor4 in solucion.items():
                if clave4 == posicion:
                    print('City: New York')
                    print('Power Supplied:', valor4, 'consumer(s)')
                    print('Covered Area:', respuesta_final, ' X ', respuesta_final, 'block(s)')
                    print('Power Deficit:', consumidores_ciudad - int(valor4), 'consumer(s)')
                    print(
                        'Ubicación dentro de la matriz de la primera posición del bloque escogido(contando de arriba hacia abajo de izquierda a derecha):',
                        clave4)










