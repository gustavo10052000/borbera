def geraGrafo():
    global grafo
    grafo = {
        '0' : ['2', '4'],
        '1' : ['2', '4'],
        '2' : ['0', '1', '3'],
        '3' : ['2'],
        '4' : ['1', '5']
    }

def largura():
    verticesVisitados = []
    for i in grafo:
        print(grafo[i])

    while(len(verticesVisitados) != len(grafo)):
        verticesVisitados.append('1')
        print('alo')

def profundidade():
    pass

def main():
    geraGrafo()
    largura()

main()