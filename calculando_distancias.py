from heapq import heappop, heappush

def menorRota(graph, origem, destino):
    distancias = {v: float('inf') for v in graph}
    distancias[origem] = 0

    heap = [(0, origem)]

    while heap:
        current_dist, atual = heappop(heap)

        if atual == destino:
            break

        if current_dist > distancias[atual]:
            continue

        for vizinho, peso in graph[atual].items():
            nova_distancia = distancias[atual] + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heappush(heap, (nova_distancia, vizinho))

    return distancias[destino]

# Grafo
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Solicitar entrada do usuário para origem e destino com verificação
origem = input("Digite o vértice de origem (A, B, C, D): ").upper()
destino = input("Digite o vértice de destino (A, B, C, D): ").upper()

# Verificar se a origem e destino são válidos
if origem not in grafo or destino not in grafo:
    print("Erro: Vértices de origem ou destino inválidos. Escolha dentre as opções: A, B, C e D.")
else:
    # Calcular a menor rota
    resultado = menorRota(grafo, origem, destino)

    # Imprimir o resultado na console
    print(f"A menor rota de {origem} para {destino} é {resultado}")
