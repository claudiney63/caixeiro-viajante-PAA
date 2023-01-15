import time

incio = time.time()


def calculo_custo_rota(grafo, rota):
    custo_pcv = 0
    vertices = range(len(grafo))

    for index in vertices:
        line = rota[index]
        column = rota[index + 1]

        peso_aresta = grafo[line][column]

        custo_pcv += peso_aresta

    return custo_pcv


def pcv_forca_bruta(grafo, rota=[0], melhor_custo=float("inf"), melhor_caminho=None):
    # Base da Recursão
    if len(rota) == len(grafo):
        # rota termina no vertice inicial
        rota.append(0)
        custo_final = calculo_custo_rota(grafo, rota)
        #print("Rota: ", rota)
        # print("Custo Final: ", custo_final)
        # print("")

        if custo_final < melhor_custo:
            melhor_caminho = rota.copy()
            melhor_custo = custo_final

        rota.pop()

        return melhor_custo, melhor_caminho

    # Etapa Recursiva
    for node in range(len(grafo)):
        if node in rota:
            continue

        rota.append(node)

        melhor_custo, melhor_caminho = pcv_forca_bruta(
            grafo, rota, melhor_custo, melhor_caminho)

        rota.pop()

    return melhor_custo, melhor_caminho


if __name__ == '__main__':
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    graph2 = [[72, 61, 15, 62, 2, 13, 7, 15],
              [62, 6, 67, 70, 10, 21, 13, 60],
              [72, 77, 32, 16, 44, 88, 26, 52],
              [62, 40, 61, 76, 59, 18, 59, 87],
              [25, 28, 85, 51, 36, 13, 59, 53],
              [29, 62, 27, 13, 60, 17, 74, 66],
              [56, 11, 28, 49, 88, 70, 38, 76],
              [63, 84, 42, 38, 40, 10, 2, 86]]

    graph3 = [[84, 25, 64, 12, 25, 80, 68, 75, 42, 62],
              [66, 50, 74, 15, 57, 61, 35, 13, 54, 76],
              [32, 6, 2, 62, 69, 44, 86, 84, 80, 48],
              [43, 9, 57, 32, 75, 40, 37, 46, 45, 85],
              [83, 12, 2, 47, 83, 60, 81, 59, 45, 73],
              [47, 65, 85, 23, 79, 55, 59, 85, 48, 68],
              [46, 33, 29, 72, 18, 37, 78, 32, 46, 83],
              [37, 87, 33, 25, 89, 64, 33, 56, 25, 16],
              [5, 25, 88, 54, 9, 70, 3, 20, 61, 8],
              [68, 26, 4, 48, 9, 29, 39, 22, 26, 29]]

pcv = pcv_forca_bruta(graph3)

print(f'Caminho Minimo: {pcv[0]}')
print(f'Rota: {pcv[1]}')

fim = time.time() - incio
print(f'Tempo de final: {fim:.5f} ms')
