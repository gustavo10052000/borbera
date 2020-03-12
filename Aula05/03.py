def geraGrafo():
    return [
            [0, 3],
            [1, 3, 5],
            [2, 4, 5],
            [3, 0, 1, 6],
            [4, 2, 8],
            [5, 1, 2, 7, 8],
            [6, 3, 7],
            [7, 5, 6],
            [8, 4, 5]
        ]


def largura(grafo, vertice):
    fila = [vertice]
    visitados = [vertice]
    while len(fila):
        n = fila.pop(0)
        for m in grafo[n]:
            if(m not in visitados):
                visitados.append(m)
                fila.append(m)
    return visitados


def profundidade(grafo, vertice, visitados):
    if vertice in visitados:
        return visitados
    visitados.append(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            visitados = profundidade(grafo, vizinho, visitados)
    return visitados


def main():
    grafo = geraGrafo()
    print(largura(grafo, 0), '\n----------------------------------')
    print(profundidade(grafo, 0, []))


main()