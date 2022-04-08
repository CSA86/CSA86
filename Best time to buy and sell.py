list = [7, 6, 4, 3, 1]

def mejor_ganancia(valor, lista):
    ganancia = 0
    for i in lista:
        if valor < i:
            temporal = i - valor
            if temporal > ganancia:
                ganancia = temporal
    return ganancia

respuesta = 0
for orden, dia in enumerate(list):
    comparativa = mejor_ganancia(dia, list[orden + 1:])
    if comparativa > respuesta:
        respuesta = comparativa

print(respuesta)