import matplotlib.pyplot as plt
import networkx as nx
import time

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
    focos = {
        'RV': {'S': 195, 'UL': 86, 'M': 178, 'BA': 180, 'Z': 91},
        'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
        'M': {'RV': 178, 'UL': 123, 'N': 170},
        'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64},
        'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230},
        'F': {'N': 230, 'S': 210, 'MA': 85},
        'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67},
        'KA': {'MA': 67, 'S': 64, 'BA': 191},
        'BA': {'KA': 191, 'RV': 180, 'Z': 85, 'BE': 91},
        'BE': {'BA': 91, 'Z': 120},
        'Z': {'BA': 120, 'BE': 85, 'RV': 91}
    }
    
    focos2 = {
        'RV': {'S': 195, 'UL': 86, 'M': 178},
        'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
        'M': {'RV': 178, 'UL': 123, 'N': 170},
        'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64},
        'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230},
        'F': {'N': 230, 'S': 210, 'MA': 85},
        'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67},
        'KA': {'MA': 67, 'S': 64}
    }
    
    focos3 = {
        'RV': {'S': 195, 'UL': 86, 'M': 178},
        'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
        'M': {'RV': 178, 'UL': 123, 'N': 170},
        'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210},
        'N': {'S': 210, 'UL': 171, 'M': 170, 'F': 230},
        'F': {'N': 230, 'S': 210},
    }
    
    focos4 = {
        'RV': {'S': 195, 'UL': 86, 'M': 178, 'BA': 180, 'Z': 91,'PS': 95, 'NF': 98},
        'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
        'M': {'RV': 178, 'UL': 123, 'N': 170, 'PS': 112,'LA': 61},
        'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64,'NF': 77},
        'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230, 'TI': 97, 'LA': 77},
        'F': {'N': 230, 'S': 210, 'MA': 85},
        'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67,'TI': 55},
        'KA': {'MA': 67, 'S': 64, 'BA': 191, 'PS': 66,'TI': 64,'NF': 56},
        'BA': {'KA': 191, 'RV': 180, 'Z': 85, 'BE': 91},
        'BE': {'BA': 91, 'Z': 120, 'PS': 81},
        'Z': {'BA': 120, 'BE': 85, 'RV': 91},
        'PS': {'RV': 95, 'M': 112, 'KA': 66, 'BE': 81,'LA': 59},
        'TI': {'N': 97,'MA': 55,'KA': 64,'LA': 85},
        'NF': {'S':77 ,'RV': 98,'KA': 56},
        'LA': {'TI': 85,'N': 77,'M': 61,'PS': 59}
    }

    # formar_grafo(focos4)

    encnontrar_caminhos('RV', focos4, [], 0)
    print("\n")
    rotas.sort()  # Ordenando as rotas

    # grafo_final(rotas[0][1], focos, "Custo Minimo")

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
    print(f'\nTempo de final: {fim:.5f} ms com N = {len(focos4)}')
