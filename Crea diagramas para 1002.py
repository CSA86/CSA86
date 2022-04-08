import random
lista = ['.', '#']
casos = random.randrange(60)
resultado = open('Diagrama para 1002.txt', 'w')
resultado.write(str(casos) + '\n')
for i in range(casos):
    for j in range(casos):
        resultado.write(random.choice(lista))
    resultado.write('\n')