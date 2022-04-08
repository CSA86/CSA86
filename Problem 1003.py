casos_a_procesar = ''
candidatos = ''
regiones = ''
valido = True
votos = []

while valido:
    print("Entre la cantidad de casos a procesar(solo escriba números en la siguiente línea):")
    try:
        casos_a_procesar=int(input())
        valido=False
    except:
        print('Introduzca un número, no letras por favor:')

for casos in range(casos_a_procesar):
    valido = True
    while valido:
        print("Para el caso", casos,",introduzca la cantidad de candidatos seguido del número de regiones:")
        datos = str(input())
        try:
            candidatos = int(datos.split()[0].strip())
        except:
            print('Introduzca un número en la posición de los candidatos, no letras por favor:')
        try:
            regiones = int(datos.split()[1].strip())
            valido = False
        except:
            print('Introduzca un número en la posición de las regiones, no letras por favor:')
        if candidatos == 1:
            print('Si existe un solo candidato, él es el ganador!!!')
    print('Para el caso', casos, 'introduzca los resultados de cada región, especificando siempre el mismo orden para cada candidato')
    for region in range(regiones):
        valido = True
        while valido:
            datos_votos = str(input())
            if len(datos_votos.split()) < candidatos:
                print('Le faltó por introducir la votación de un candidato en esta region')
                datos_votos = ''
            elif len(datos_votos.split()) > candidatos:
                print('Introdujo datos para', len(datos_votos.split()), 'y solo son', candidatos, 'candidatos')
                datos_votos = ''
            for valor in datos_votos.split():
                try:
                    if type(int(valor)) == int:
                        pass
                except:
                    print('Introdujo una letra')
                    datos_votos = ''
            if not datos_votos:
                print('Por favor, introduzca nuevamente los datos para esta región')
            else:
                valido = False
        posicion = -1
        voto = ''
        if region == 0:
            for cada in datos_votos.split():
                votos.append(int(cada))
        else:
            for voto in datos_votos.split():
                posicion += 1
                votos[posicion] += int(voto)
        mayor_voto = 0
        posicion = -1
        lista_empatados = []
        if region == regiones - 1:
            for politico in votos:
                if int(politico) > mayor_voto:
                    mayor_voto = politico
            if votos.count(mayor_voto) > 1:
                print('Existió un empate, a continuación una lista de los candidatos que empataron:')
                for empatados in votos:
                    posicion += 1
                    if empatados == mayor_voto:
                        lista_empatados.append(posicion)
                print(lista_empatados)
            else:
                print('El ganador es el candidato:', votos.index(mayor_voto))
