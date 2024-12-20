matriz_adjacencia = [
    [0, 4, 1, float('inf'), float('inf')],
    [4, 0, 2, 1, float('inf')],
    [1, 2, 0, 5, float('inf')],
    [float('inf'), 1, 5, 0, 3],
    [float('inf'), float('inf'), float('inf'), 3, 0]
]

visitados = []
tabela = []

def inicializa_tabela(matriz_adjacencia):
    num_linhas = len(matriz_adjacencia)
    
    for i in range(num_linhas):
        if i == 0:
            tabela.append({"vertice": i, "custo": 0, "anterior": None})
        else:
            tabela.append({"vertice": i, "custo": float('inf'), "anterior": None})

def encontrar_prox_vertice():
    menor_custo = float('inf')
    vertice = None
    
    for row in tabela:
        if row["vertice"] not in visitados and row["custo"] < menor_custo:
            menor_custo = row["custo"]
            vertice = row["vertice"]
    
    return vertice

def dijkstra():
    vertice_atual = 0
    visitados.append(vertice_atual)
    while(len(visitados) < len(matriz_adjacencia)):
        i = 0
        while(i < len(matriz_adjacencia)):
            custo = matriz_adjacencia[vertice_atual][i]
            if custo != 0 and custo != float('inf'):
                if tabela[i]["custo"] > tabela[vertice_atual]["custo"] + custo:
                    tabela[i]["custo"] = tabela[vertice_atual]["custo"] + custo
                    tabela[i]["anterior"] = vertice_atual
            i += 1
        vertice_atual = encontrar_prox_vertice()
        visitados.append(vertice_atual)

def refazer_caminho(vertice_destino):
    caminho = []
    atual = vertice_destino
    
    while atual is not None:
        caminho.insert(0, atual)
        atual = tabela[atual]["anterior"]
    return caminho


inicializa_tabela(matriz_adjacencia)

vertice_origem = 0
vertice_destino = 4

dijkstra()
caminho = refazer_caminho(vertice_destino)

print("Tabela final:", tabela)
print("Visitados:", visitados)
print("Caminho do vertice", vertice_origem, "ate o vertice", vertice_destino, ":", caminho)
