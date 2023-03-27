import heapq
import exemlos as ex

def dijkstra_caminho_curto(graph, start, end):
    distancias = {node: float('inf') for node in graph}

    previa = {node: None for node in graph}
    distancias[start] = 0    

    queue = [(0, start)]

    while queue:
        distancia_atual, node_atual = heapq.heappop(queue)

        if node_atual == end:
            caminho = []
            while node_atual is not None:
                caminho.append(node_atual)
                node_atual = previa[node_atual]
            return distancia_atual, list(reversed(caminho))

        for neighbor, weight in graph[node_atual].items():
            distance = distancia_atual + weight
            if distance < distancias[neighbor]:
                distancias[neighbor] = distance
                previa[neighbor] = node_atual
                heapq.heappush(queue, (distance, neighbor))

    return float('inf'), []

def heuristica(graph, start, priori):
    caminhofinal=[]
    pesofinal=0
    peso, caminho = dijkstra_caminho_curto(graph, start, priori)
    caminhofinal.append(caminho)
    pesofinal+=peso

    for ca in caminho: #remove os vertices ja percorridos
        if ca in cities:
            cities.remove(ca)

    while(cities!=[]): #continua ate a lista de vertices não percorridos não ser vazia
        noatual=caminho[-1]

        cont=0
        atual = float('inf')
        for i in graph:
            if i==noatual:

                for j in graph[i]:
                    if j in cities:
                        if graph[i][j]<=atual:
                            atual=graph[i][j]
                            atualkey=j
                            cont+=1
        if cont==0:
            dist=float('inf')
            for ct in cities:
                peso, caminho = dijkstra_caminho_curto(graph, noatual, ct)
                
                if peso<dist:
                    dist=peso
                    caminho=caminho

            cities.remove(caminho[-1])
            noatual=caminho[-1]
            caminhofinal.append(caminho)
            pesofinal+=peso

        else:
            peso,caminho = dijkstra_caminho_curto(graph, noatual, atualkey)
            cities.remove(caminho[-1])
            noatual=caminho[-1]
            caminhofinal.append(caminho)
            pesofinal+=peso

    peso, caminho = dijkstra_caminho_curto(graph, noatual, start)
    caminhofinal.append(caminho)
    pesofinal += peso

    # print(pesofinal)
    listaprint = []
    for i in range(len(caminhofinal)):
        if i!=len(caminhofinal)-1:
            for j in range (len(caminhofinal[i])-1):
                listaprint.append(caminhofinal[i][j])

        else:
            for j in range(len(caminhofinal[i])):
                listaprint.append(caminhofinal[i][j])
    # print(listaprint)

    return pesofinal, listaprint

if __name__ == "__main__":

    cities = []

    for c in ex.focos4:
        cities.append(c)

    peso, caminho = heuristica(ex.focos4, 'RV', 'Z')

    print(f'Peso: {peso}')
    print(f'Caminho Percorrido: {caminho}')