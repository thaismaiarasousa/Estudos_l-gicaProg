from collections import deque

def pesquisa(grafo, nome, condicao_vendedor):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if condicao_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga")
                return pessoa, verificadas
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)

    return None, verificadas

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'  # Exemplo: Verifica se o nome termina com 'm'

# Exemplo de uso:
grafo = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

vendedor_encontrado, pessoas_verificadas = pesquisa(grafo, "voce", pessoa_e_vendedor)

if vendedor_encontrado:
    print("Vendedor encontrado:", vendedor_encontrado)
else:
    print("Nenhum vendedor encontrado.")

print("Pessoas verificadas:", pessoas_verificadas)
