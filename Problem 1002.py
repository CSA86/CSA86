valido = True
lado_del_cuadrado = 0

def analiza_la_fila(fila, columna):
    potencial_fila = 0
    for valor_columna in fila[columna:]:
        if valor_columna == '.':
            potencial_fila += 1
        else:
            break
    return potencial_fila


print('Este programa encuentra el mayor área cuadrada dentro de un área cuadrada que posee espacios libres y con obstáculos')
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
        print('Para el caso', casos, 'introduzca el lado del área cuadrada a analizar')
        try:
            lado_del_cuadrado = int(input())
            valido = False
        except:
            print('Por favor introduzca un número, no letras, intente nuevamente')
    print('Introduzca . para área libre y # para los obstáculos')
    for fila in range(lado_del_cuadrado):
        valido = True
        while valido:
            datos_fila = str(input())
            if (datos_fila.count('#') + datos_fila.count('.')) != lado_del_cuadrado:
                print('Existen símbolos erróneos o la cantidad de caracteres no coincide con la longitud del lado')
                datos_fila = ''
            if len(datos_fila) > lado_del_cuadrado:
                print('Los datos introducido superan la longitud del área')
                datos_fila = ''
            elif datos_fila and len(datos_fila) < lado_del_cuadrado:
                print('Los datos introducidos no alcanzan la longitud del área')
                datos_fila = ''
            elif len(datos_fila) == lado_del_cuadrado:
                valido = False
                cuadrado.append(datos_fila)
    #print(cuadrado)
    respuesta = 0
    posible_respuesta = 0
    for orden_fila, valor_fila in enumerate(cuadrado):
        for orden_columna, valor_columna in enumerate(valor_fila):
            potencial_fila = 0
            potencial_columna = 0
            if valor_columna == '.':
                potencial_fila = analiza_la_fila(valor_fila, orden_columna)
                if potencial_fila > 1:
                    potencial_columna += 1
                    potencial_proxima_fila = 0
                    #print(orden_fila, orden_columna, potencial_fila, potencial_columna)
                    for valor_proxima_fila in cuadrado[orden_fila+1:]:
                        potencial_proxima_fila = analiza_la_fila(valor_proxima_fila, orden_columna)
                        if potencial_proxima_fila >= potencial_fila:
                            potencial_columna += 1
                            #print(orden_fila, orden_columna, potencial_proxima_fila, potencial_columna)
                        else:
                            break
                    if potencial_fila < potencial_columna:
                        posible_respuesta = potencial_fila
                    else:
                        posible_respuesta = potencial_columna
            if posible_respuesta > respuesta:
                respuesta = posible_respuesta
                print('APORTA RESPUESTA:', orden_fila, orden_columna, respuesta)
    print(respuesta)



