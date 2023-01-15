import time
import numpy as np

incio = time.time()

lista_rotas = {}

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
        # print("Rota: ", rota)
        rota_aux = []
        for i in rota:
            rota_aux.append(i)

        lista_rotas[custo_final] = rota_aux
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


def escolher_priori(matriz, priori):
    matriz_aux = matriz
    for i in range(priori+1):
        if (i != priori):
            matriz_aux[i][priori] = -1
            matriz_aux[priori][i] = -1

    return matriz_aux


def encontra_priori(graph_priori):
    pcv_priori = pcv_forca_bruta(graph_priori)
    return pcv_priori


if __name__ == '__main__':
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    graph2 = [[69, 68, 67, 31, 51, 35],
              [72, 12, 85, 66, 55, 9],
              [11, 74, 84, 36, 81, 49],
              [70, 33, 4, 31, 74, 55],
              [38, 9, 32, 34, 12, 57],
              [76, 4, 62, 71, 40, 40]]

    # graph2 = [[72, 61, 15, 62, 2, 13, 7, 15],
    #           [62, 6, 67, 70, 10, 21, 13, 60],
    #           [72, 77, 32, 16, 44, 88, 26, 52],
    #           [62, 40, 61, 76, 59, 18, 59, 87],
    #           [25, 28, 85, 51, 36, 13, 59, 53],
    #           [29, 62, 27, 13, 60, 17, 74, 66],
    #           [56, 11, 28, 49, 88, 70, 38, 76],
    #           [63, 84, 42, 38, 40, 10, 2, 86]]

    # graph3 = [[84, 25, 64, 12, 25, 80, 68, 75, 42, 62],
    #           [66, 50, 74, 15, 57, 61, 35, 13, 54, 76],
    #           [32, 6, 2, 62, 69, 44, 86, 84, 80, 48],
    #           [43, 9, 57, 32, 75, 40, 37, 46, 45, 85],
    #           [83, 12, 2, 47, 83, 60, 81, 59, 45, 73],
    #           [47, 65, 85, 23, 79, 55, 59, 85, 48, 68],
    #           [46, 33, 29, 72, 18, 37, 78, 32, 46, 83],
    #           [37, 87, 33, 25, 89, 64, 33, 56, 25, 16],
    #           [5, 25, 88, 54, 9, 70, 3, 20, 61, 8],
    #           [68, 26, 4, 48, 9, 29, 39, 22, 26, 29]]

    # graph4 = [[75, 82, 15, 44, 68, 28, 56, 60, 3, 89, 81],
    #           [86, 43, 16, 3, 63, 80, 25, 48, 42, 56, 70],
    #           [44, 14, 25, 89, 61, 55, 45, 68, 61, 12, 35],
    #           [86, 21, 22, 67, 31, 10, 25, 84, 72, 47, 64],
    #           [13, 35, 45, 56, 51, 5, 61, 37, 14, 6, 83],
    #           [88, 35, 42, 31, 64, 39, 87, 32, 41, 61, 18],
    #           [39, 62, 30, 8, 55, 46, 53, 26, 64, 12, 63],
    #           [70, 57, 3, 13, 90, 2, 27, 76, 81, 74, 76],
    #           [2, 42, 15, 72, 44, 50, 84, 52, 45, 16, 53],
    #           [6, 29, 35, 25, 52, 62, 73, 30, 25, 57, 87],
    #           [1, 60, 10, 83, 81, 22, 35, 17, 62, 20, 6]]


    grafo = graph2

    pcv_real = pcv_forca_bruta(grafo) #gera a rota e peso minimo (real)
    print(lista_rotas)
    rotas_reais = lista_rotas.copy()

    graph_priori = escolher_priori(grafo, 3)
    pcv_priori = encontra_priori(graph_priori) #gera a rota e peso minimo (prioritario)

    custo_minimo_priori = pcv_priori[0]
    rota_escolhida = pcv_priori[1]

    rota_priori = []
    custo_final_real = 0

    for i in rotas_reais:
        if(rotas_reais[i] == rota_escolhida):
            rota_priori = rota_escolhida
            custo_final_real = i

    print(f'\nCusto Minimo (real): {pcv_real[0]}')
    print(f'Rota: {pcv_real[1]}')

    print(f'\nCusto Minimo (real): {custo_final_real}')
    print(f'Rota: {rota_priori}')

    print(f'\nCusto Minimo (prioridade): {custo_minimo_priori}')
    print(f'Rota: {rota_escolhida}')

    fim = time.time() - incio
    print(f'\nTempo de final: {fim:.5f} ms')
