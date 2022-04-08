matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

filas = len(matrix)
columnas = len(matrix[0])

nueva_matriz = []
for j in range(columnas):
    temporal = []
    for i in range(filas):
        temporal.append(0)
    nueva_matriz.append(temporal)

for orden, fila in enumerate(matrix):
    print(fila)

print('----------------------------------------------')

for i in range(filas):
    for j in range(columnas):
        nueva_matriz[j][filas - i - 1] = matrix[i][j]

for orden, fila in enumerate(nueva_matriz):
    print(fila)