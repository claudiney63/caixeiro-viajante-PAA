import heapq

def dijkstra_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}

    previous = {node: None for node in graph}
    distances[start] = 0    

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return current_distance, list(reversed(path))

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return float('inf'), []

def heuristica(graph, start, priori):
    caminhofinal=[]
    pesofinal=0
    peso, caminho = dijkstra_shortest_path(graph, start, priori)
    caminhofinal.append(caminho)
    pesofinal+=peso
    for ca in caminho:
        if ca in cities:
            cities.remove(ca)
    while(cities!=[]):
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
                peso, caminho = dijkstra_shortest_path(graph, noatual, ct)
                if peso<dist:
                    dist=peso
                    path=caminho
            cities.remove(path[-1])
            noatual=path[-1]
            caminhofinal.append(path)
            pesofinal+=peso
        else:
            peso,caminho = dijkstra_shortest_path(graph, noatual, atualkey)
            cities.remove(caminho[-1])
            noatual=caminho[-1]
            caminhofinal.append(caminho)
            pesofinal+=peso

    peso, caminho = dijkstra_shortest_path(graph,noatual,start)
    caminhofinal.append(caminho)
    pesofinal+=peso

    print(pesofinal)
    listaprint=[]
    for i in range(len(caminhofinal)):
        if i!=len(caminhofinal)-1:
            for j in range (len(caminhofinal[i])-1):
                listaprint.append(caminhofinal[i][j])
        else:
            for j in range(len(caminhofinal[i])):
                listaprint.append(caminhofinal[i][j])
    print(listaprint)

if __name__ == "__main__":

    cities = []

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
    
    for c in focos4:
        cities.append(c)

    heuristica(focos4, 'RV', 'Z')

    # distance, path = dijkstra_shortest_path(focos3, 'RV', 'F')
    # print(distance)  # 5
    # print(path)  # ['A', 'C', 'D']