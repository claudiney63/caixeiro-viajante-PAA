import matplotlib.pyplot as plt
import networkx as nx
import time
import exemlos as ex

incio = time.time()

rotas = []

posicao_priori = 99999
prioridade = 99999

def encnontrar_caminhos(inicio, focos, caminho, distancia):
    # Adiciona nó inicial
    caminho.append(inicio)

    # Calcula o comprimento do caminho do atual ao último nó
    if len(caminho) > 1:
        distancia += focos[caminho[-2]][inicio]

    # Se o caminho contém todas as focos e não é um beco sem saída,
    # adiciona o caminho da última para a primeira local e retorna.
    if (len(focos) == len(caminho)) and (caminho[0] in focos[caminho[-1]]):
        global rotas
        caminho.append(caminho[0])
        distancia += focos[caminho[-2]][caminho[0]]
        # print (caminho, distancia)
        rotas.append([distancia, caminho])
        return

    # Caminhos de bifurcação para todas as focos possíveis ainda não utilizadas
    for local in focos:
        if (local not in caminho) and (inicio in focos[local]):
            encnontrar_caminhos(local, dict(focos), list(caminho), distancia)

def formar_grafo(focos):
    G = nx.Graph()
    for i in focos:
        for j in focos[i]:
            G.add_edge(i, j, weight=focos[i][j])

    plt.figure("Grafo")
    pos = nx.layout.planar_layout(G)
    nx.draw(G, pos=pos, with_labels=True)
    peso_aresta = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, peso_aresta)
    plt.show()


def grafo_final(rota, focos, label):
    H = nx.Graph()
    for i in range(len(rota)-1):

        for c in focos:
            if(rota[i] == c):
                vertice1 = c
                for j in focos[c]:
                    if(rota[i+1] == j):
                        vertice2 = j
                        peso = focos[c][j]

        print(f'{vertice1} e {vertice2} e {peso}')
        H.add_edge(vertice1, vertice2, weight = peso)

    plt.figure(label)
    pos = nx.layout.planar_layout(H)
    nx.draw(H, pos=pos, with_labels=True)
    peso_aresta = nx.get_edge_attributes(H, "weight")
    nx.draw_networkx_edge_labels(H, pos, peso_aresta)
    plt.show()


if __name__ == '__main__':

    encnontrar_caminhos('RV', ex.focos4, [], 0)
    print("\n")
    rotas.sort()  # Ordenando as rotas

    if len(rotas) != 0:
        print(f"Menor Custo e Rota: {rotas[0]}")
        for i in range(len(rotas)):
            for j in range(len(rotas[0][1])):
                if rotas[i][1][j] == 'N' and j < posicao_priori:
                    posicao_priori = j
                    prioridade = i
    else:
        print("ERROR!")

    print(f'Custo e Rota com Prioridade: {rotas[prioridade][0], rotas[prioridade][1]}')
    fim = time.time() - incio
    print(f'\nTempo de final: {fim:.5f} ms com N = {len(ex.focos4)}')
