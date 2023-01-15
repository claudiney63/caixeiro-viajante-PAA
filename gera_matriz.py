import random

tam = 6

matriz = []

for c in range(0, tam):
    matriz.append([])
    for i in range(0, tam):
        matriz[c].append(random.randint(1, 90))

    print(matriz[c],",")

