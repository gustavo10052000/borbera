import os
global grafo
grafo = []

def insertGrafo():
    grafo = []
    vertices = int(input("Informe a quantidade de vértices do grafo:\n"))
    for i in range(vertices):
        grafo.append([])
        for j in range(vertices):
            grafo[i].append(0)

    printGrafo(grafo)

def updateAdjacency():
    verticex = int(input("Informe o primeiro vértice:\n"))
    verticey = int(input("Informe o primeiro vértice:\n"))

    reference = grafo[verticex][verticey]

    if (reference == 0):
        grafo[verticex][verticey] = 1
        grafo[verticey][verticex] = 1
    else:
        grafo[verticex][verticey] = 0
        grafo[verticey][verticex] = 0

    printGrafo(grafo)

def printGrafo(grafo):
    os.system('cls')
    for i in range(len(grafo)):
        print(grafo[i])

def main():
    os.system('cls')
    while True:
        if (grafo == []):
            print("===========================\n Grafo ainda não declarado\n===========================\n")
        else:
            printGrafo(grafo)

        options = int(input("1 -> Gerar Novo Grafo\n2 -> Atualizar alguma aresta do grafo\n3 -> Sair\n\n"));
        if (options == 1):
            os.system('cls')
            insertGrafo()
        elif (options == 2):
            os.system('cls')
            if (grafo == []):   
                pass
            else:
                updateAdjacency()

        elif (options == 3):
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Comando não reconhecido!")

main()