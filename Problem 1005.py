import operator

def sortSecond(val):
    return val[1]

def arma_matriz(fila):
    matriz = []
    for posicion in range(fila):
        matriz.append([0]*3)
    return matriz

print('Este juego determina la forma óptima de rentar un vehículo a partir de las propuestas de renta realizadas por los clientes')
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
    inicio = []
    fin = []
    precio = []
    while valido:
        print("Entre la cantidad de pedidos para el caso", casos, ",(solo escriba números en la siguiente línea):")
        try:
            pedidos = int(input())
            valido = False
        except:
            print('Introduzca un número, no letras por favor:')
    matriz = arma_matriz(pedidos)
    print(matriz)
    for pedido in range(pedidos):
        valido = True
        while valido:
            if pedido == 0:
                print('Para cada pedido del caso', casos, 'introduzca la hora de inicio, la hora de fin y el precio que pagaría el cliente')
            detalles_del_pedido = str(input())
            try:
                hora_inicio = int(detalles_del_pedido.split()[0].strip())
                hora_fin = int(detalles_del_pedido.split()[1].strip())
                importe = int(detalles_del_pedido.split()[2].strip())
                if hora_inicio < hora_fin:
                    inicio.append(hora_inicio)
                    fin.append(hora_fin)
                    precio.append(importe)
                    matriz[pedido][0] = hora_inicio
                    matriz[pedido][1] = hora_fin
                    matriz[pedido][2] = importe
                    valido = False
                else:
                    print('Vuelva a introducir los datos, la hora de inicio no puede ser mayor que la hora de fin')
            except:
                print('Por favor introduzca números solamente en los detalles del pedido, no letras, intente nuevamente')
    #print(matriz)
    copia_matriz = matriz.copy()
    matriz.sort(key=sortSecond)#Se ordena la matriz en base al 2do elemento que es la hora final
    matriz_ordenada = matriz
    relacion_entre_matriz_ordenada_y_sin_ordenar = {}
    #print(matriz)
    for orden,item in enumerate(matriz_ordenada):
        indice_orden = copia_matriz.index(item)
        relacion_entre_matriz_ordenada_y_sin_ordenar.update({orden: indice_orden})
    #print(relacion_entre_matriz_ordenada_y_sin_ordenar)
    matriz_respuesta = {}
    for orden,fila in enumerate(matriz): #se recorre la matriz
        contador = 0
        diccionario_temporal = {}
        for proximo_numero, proxima_fila in enumerate(matriz[orden + 1:]):
            if fila[1] <= proxima_fila[0]:#si la hora final del caso analizado es menor que la hora de inicio del caso que le sigue, se suma el importe y se analiza hacia adelante
                contador += 1
                coordenadas = str(orden)+str(proximo_numero+orden+1)
                matriz_respuesta.update({coordenadas: fila[2] + proxima_fila[2]})
                for clave, valor in matriz_respuesta.items():
                    variable = str(clave)
                    variable = variable[-1]
                    if variable == str(orden):
                        nueva_clave = clave[0:len(clave)-1]
                        nueva_clave = nueva_clave+str(coordenadas)
                        importe = int(valor)+int(proxima_fila[2])
                        diccionario_temporal.update({nueva_clave:int(valor)+int(proxima_fila[2])})
            matriz_respuesta.update(diccionario_temporal)
        if contador == 0:
            matriz_respuesta.update({str(orden): fila[2]})
    resultado = sorted(matriz_respuesta.items(), key=operator.itemgetter(1))
    resultado.reverse()
    #print(resultado[0])
    a = resultado[0]
    variable1 = ''
    resultado_real = {}
    for orden1, valor1 in enumerate(a):
        if orden1 == 0:
            for i in valor1:
                for clave1, valor_real in relacion_entre_matriz_ordenada_y_sin_ordenar.items():
                    if str(i) == str(clave1):
                        variable1 = variable1+str(valor_real)
    resultado_real.update({variable1: a[1]})
    print(resultado_real)











