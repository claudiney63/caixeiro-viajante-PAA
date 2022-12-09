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
    # Recursion base
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

    # Recursive step
    for node in range(len(grafo)):
        if node in rota:
            continue

        rota.append(node)

        melhor_custo, melhor_caminho = pcv_forca_bruta(
            grafo, rota, melhor_custo, melhor_caminho)

        rota.pop()

    return melhor_custo, melhor_caminho


if __name__ == '__main__':
    n = 4
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

pcv = pcv_forca_bruta(graph)

print(f'Caminho Minimo: {pcv[0]}')
print(f'Rota: {pcv[1]}')

fim = time.time() - incio
print(f'Tempo de final: {fim:.5f} ms')
