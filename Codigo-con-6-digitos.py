import itertools

def suma(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def producto(lista):
    producto = 0
    for orden, elemento in enumerate(lista):
        if orden == 0:
            producto = elemento
        else:
            producto = producto * elemento
    return producto


valores = [i for i in range(1, 7)]

conteo_de_sumas = {}
conteo_de_productos = {}

for i in range(2, 7):
    for comb in itertools.combinations(valores, i):
        la_suma = suma(comb)
        if la_suma not in conteo_de_sumas:
            conteo_de_sumas.update({la_suma: 1})
        else:
            valor = conteo_de_sumas[la_suma] + 1
            conteo_de_sumas.update({la_suma: valor})
        el_producto = producto(comb)
        if el_producto not in conteo_de_productos:
            conteo_de_productos.update({el_producto: 1})
        else:
            valor = conteo_de_productos[el_producto] + 1
            conteo_de_productos.update({el_producto: valor})
        print(comb, la_suma, el_producto)

print('Sumas:', conteo_de_sumas)
print('Productos:', conteo_de_productos)