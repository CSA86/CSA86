def calcula_binario(numero):
    ejecutar = True
    binario = []
    while ejecutar:
        binario.append(numero % 2)
        numero = numero // 2
        if numero == 0:
            ejecutar = False
    binario.reverse()
    return binario

def adecuar_longitud(lista):
    longitud_binaria = len(lista[-1])
    for orden, caso in enumerate(lista):
        if len(caso) < longitud_binaria:
            cant_ceros_adicionar = longitud_binaria - len(caso)
            for i in range(cant_ceros_adicionar):
                caso.insert(0, 0)
            lista[orden] = caso
    return lista

def calcula_suma(lista1, lista2):
    for i in range(len(lista1)):
        lista1[i] = lista1[i] + lista2[i]
    return lista1


def comprueba_si_suma_indica_rota(original, posicion, actual, roto):
    suma = original[0].copy()
    for orden, caso in enumerate(original):
        if orden != posicion:
            suma = calcula_suma(suma, caso)
        else:
            suma = calcula_suma(suma, actual)
    for orden, caso in enumerate(suma):
        suma[orden] = caso % 2
    roto_en_binario = calcula_binario(roto)
    if len(roto_en_binario) < len(original[-1]):
        ceros_anadir = len(original[-1]) - len(roto_en_binario)
        for i in range(ceros_anadir):
            roto_en_binario.insert(0, 0)
    if suma == roto_en_binario:
        return True
    else:
        return False

valido = True
while valido:
    print("Entre la cantidad de CPU - 1 (el orden comienza en cero):")
    try:
        decimal = int(input())
        valido = False
    except:
        print('Introduzca un número, no letras por favor:')

intervalo_en_binario = []
for i in range(decimal + 1):
    intervalo_en_binario.append(calcula_binario(i))

lista_de_num_en_binario = adecuar_longitud(intervalo_en_binario)
#for num in lista_de_num_en_binario:
#    print(num)

valido = True
while valido:
    print("Entre la posicion de la CPU rota:")
    try:
        posicion_de_la_rota = int(input())
        if posicion_de_la_rota <= decimal:
            valido = False
        else:
            print('Entre una posicion válida')
    except:
        print('Introduzca un número, no letras por favor:')


estado_de_los_switch = []
for i in range(decimal + 1):
    valido = True
    while valido:
        print("Diga el estado del switch", i)
        try:
            estado = int(input())
            if estado >= 0 and estado <= 1:
                valido = False
                estado_de_los_switch.append(estado)
            else:
                print('Entre 0 o 1')
        except:
            print('Introduzca un número, no letras por favor:')

#Aqui se posicionan los switch como realmente estan
for orden, state in enumerate(estado_de_los_switch):
    if state == 0:
        lista_de_num_en_binario[orden] = lista_de_num_en_binario[0]

#aqui se prueba que resultado provoca la conmutacion del switch:
#si la suma indica el roto se aborta
for orden, state in enumerate(estado_de_los_switch):
    if state == 0:
        temporal = calcula_binario(orden) #Si esta apagado se encienden
        if len(temporal) < len(lista_de_num_en_binario[-1]):
            ceros_a_adicionar = len(lista_de_num_en_binario[-1]) - len(temporal)
            for i in range(ceros_a_adicionar):
                temporal.insert(0, 0)
    else:
        temporal = lista_de_num_en_binario[0] #Si estan encendidos se apagan
    respuesta = comprueba_si_suma_indica_rota(lista_de_num_en_binario, orden, temporal, posicion_de_la_rota)
    if respuesta:
        if state == 0:
            print('Encender el switch', orden)
        else:
            print('Apagar el switch', orden)
        break







