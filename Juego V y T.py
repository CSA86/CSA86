from random import randint,uniform,random
adivino=False
contador=0
sirve=False
lista_numero_a_adivinar=[]
lista_numero_intento=[]
respuesta=[]

def valida_numero_del_intento (numero_intento):
    lista_numero_intento=[]
    m = int(numero_intento / 1000)
    c = int((numero_intento - 1000 * m) / 100)
    d = int((numero_intento - 1000 * m - 100 * c) / 10)
    u = int(numero_intento - (1000 * m + 100 * c + 10 * d))
    if numero_intento<100:
        print(" Los números de 2 cifras no son una opción válida")
        return False
    elif m==c or m==d or m==u or c==d or c==u or d==u:
        print("Los números con cifras repetidas no son una opción válida")
        return False
    else:
        lista_numero_intento.append(m)
        lista_numero_intento.append(c)
        lista_numero_intento.append(d)
        lista_numero_intento.append(u)
        return lista_numero_intento

def cuenta_vacas(num_sistema,num_player):
    vaca = 0
    for recorre_num_sistema in range(0,4):
        for recorre_num_player in range(0, 4):
            if recorre_num_sistema!=recorre_num_player and num_sistema[recorre_num_sistema]==num_player[recorre_num_player]:
                vaca+=1
    return vaca

def cuenta_toros(system_num,player_num):
    toro = 0
    for s in range(0,4):
        for p in range(0, 4):
            if s==p and system_num[s]==player_num[p]:
                toro+=1
    return toro

def number_to_adivinate():
    sirve=False
    while sirve==False:
        numero_a_adivinar=randint(1,9999)
        millar=int(numero_a_adivinar/1000)
        centena=int((numero_a_adivinar-1000*millar)/100)
        decena=int((numero_a_adivinar-1000*millar-100*centena)/10)
        unidad=int(numero_a_adivinar-(1000*millar+100*centena+10*decena))
        if millar==centena or millar==decena or millar==unidad or centena==decena or centena==unidad or decena==unidad:
            sirve=False
        else:
            sirve=True
            lista_numero_a_adivinar.append(millar)
            lista_numero_a_adivinar.append(centena)
            lista_numero_a_adivinar.append(decena)
            lista_numero_a_adivinar.append(unidad)
    return lista_numero_a_adivinar

numero_a_adivinar=number_to_adivinate()
while adivino == False:
    contador+=1
    respuesta=False
    intento=0
    while respuesta==False:
        try:
            intento = int(input("Introduzca un número para su intento\n"))
        except:
            continue
        respuesta=0
        respuesta=valida_numero_del_intento(intento)
    respuesta_toros=cuenta_toros(numero_a_adivinar,respuesta)
    respuesta_vacas=cuenta_vacas(numero_a_adivinar,respuesta)
    if respuesta_toros==4:
        print('Felicidades, ud. ha adivinado el número')
        adivino=True
        exit()
    else:
        print("Respuesta para su intento",contador,". Toros:",respuesta_toros,"Vacas:",respuesta_vacas)