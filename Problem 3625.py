def movimientos_posibles(caso,mov):
    dif=caso-mov
    movida_posible=[]
    if dif % 3 == 0:
        for i in range(1, int(dif / 3)):
            movida_posible.append(i)
    else:
        for i in range(1, int(dif / 3) + 1):
            movida_posible.append(i)
    i = 0
    while i < len(movida_posible):
        if caso-(mov+movida_posible[i])== 6:
            del movida_posible[i]
        else:
            i += 1
    return movida_posible


valido=True
while valido:
    print("Entre la cantidad de casos a procesar(solo escriba números en la siguiente línea):")
    try:
        casos_a_procesar=int(input())
        valido=False
    except:
        print('Introduzca un número, no letras por favor:')
print('Para cada caso introduzca la cantidad de piedras que habrá en la pila al inicio del juego')
for casos in range(casos_a_procesar):
    valido = True
    while valido:
        entrada_del_usuario = str(input())
        try:
            dato = int(entrada_del_usuario.split()[0].strip())
            valido=False
        except:
            print('Por favor introduzca números, no letras, intente nuevamente')

movimientos_del_turno=[]
movimientos_del_turno=movimientos_posibles(dato,0)
#print(movimientos_del_turno)
a=len(movimientos_del_turno)
seguir_el_ciclo=True
jugada=1
while seguir_el_ciclo:
    jugada+=1
    segunda_movida=[]
    for i in movimientos_del_turno:
        if int(dato) - int(i) <= 3:
            if int(dato) - int(i) == 3 or int(dato) - int(i) == 1:
                segunda_movida.append(1)
            else:
                segunda_movida.append(2)
        else:
            segunda_movida.append(movimientos_posibles(dato,i))
    for orden,valor in enumerate(movimientos_del_turno):
        for orden1,valor1 in enumerate(segunda_movida):
            if orden == orden1:
                if type(valor1)!= int:
                    for k in valor1:
                        #temporal=str(valor)+'-'+str(k)
                        temporal=valor+k
                        if temporal<=dato:
                            movimientos_del_turno.append(temporal)
                else:
                    #temporal = str(valor) + '-' + str(valor1)
                    temporal = valor + valor1
                    if temporal<=dato:
                        movimientos_del_turno.append(temporal)
    del movimientos_del_turno[:a]
    prueba=list(set(movimientos_del_turno))
    movimientos_del_turno=prueba
    #print(movimientos_del_turno)
    if len(movimientos_del_turno)>0:
        c=0
        for l in movimientos_del_turno:
            if l==dato:
                c+=1
        if c==len(movimientos_del_turno):
            seguir_el_ciclo=False
        else:
            seguir_el_ciclo =True
    else:
        seguir_el_ciclo = False
        jugada-=1
if jugada%2==0:
    print('Gana el segundo jugador')
else:
    print('Gana el 1er jugador')
#print(jugada)





