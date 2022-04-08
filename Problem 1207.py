#El problema del recibo de electricidad combinado con el vecino
def calcula_consumo_total(importe):
    if importe<=200:
        consumo=importe/2
    elif importe>=203 and importe<=30200:
        consumo=((importe-200)/3)+100
    elif importe>=30205 and importe<=5030200:
        consumo=((importe-30200)/5)+10100
    else:
        consumo=((importe-5030200)/7)+1010100
    return consumo

def calcula_importe_del_consumo(consumido):
    if consumido<=100:
        importe=consumido*2
    elif consumido>=101 and consumido<=10000:
        importe=(consumido-100)*3+200
    elif consumido>=10001 and consumido<=1000000:
        importe=(consumido-10000)*5+29900
    else:
        importe=(consumido-1000000)*7+4979900
    return importe

valido=True
otro_caso=True
c=-1
casos={}
a=0
b=0
while valido and otro_caso:
    c+=1
    if c==0:
        print("Introduzca los dos valores de cada caso en una línea, para finalizar coloque dos ceros en la línea")
    datos = str(input())
    try:
        a = int(datos.split()[0].strip())
    except:
        print('Introduzca números no letras por favor:')
    try:
        b = int(datos.split()[1].strip())
    except:
        print('Introduzca números no letras por favor:')
    if a==0 and b==0:
        otro_caso=False
    else:
        casos.update({a:b})
#print(casos)
for clave, valor in casos.items():
    variable=clave
    consum=calcula_consumo_total(variable)
    #print('Consumo total',consum)
    if consum%2==0:
        for i in range(1,int(consum/2)+1):
            j=consum-i
            consumo_mio=calcula_importe_del_consumo(i)
            consumo_del_vecino=calcula_importe_del_consumo(j)
            if consumo_del_vecino-consumo_mio==valor:
                print('Mi consumo real es:',consumo_mio)
                print('Me ahorro',clave-(consumo_mio+consumo_del_vecino))
    else:
        for i in range(1,int(consum/2)):
            j = consum - i
            consumo_mio = calcula_importe_del_consumo(i)
            consumo_del_vecino = calcula_importe_del_consumo(j)
            if consumo_del_vecino - consumo_mio == valor:
                print('Mi consumo real es:', consumo_mio)
                print('Me ahorro', clave - (consumo_mio + consumo_del_vecino))