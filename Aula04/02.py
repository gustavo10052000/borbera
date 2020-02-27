import time
import os
global matriz
matriz = []


def clear():
    if os.name == "nt":
        os.system("clear")
    else:
        os.system("cls")


def listaAdjacencia():
    clear()
    v = int(input("Informe a quantidade de vertices: \n"))
    for i in range(v):
        vertice = ''
        linha = []
        while vertice != '0':
            vertice = input("Informe o elemento para inserir na matriz (digite 0 para ir a proxima):\n")
            if (vertice != '0'):
                linha.append(vertice)
        matriz.append(linha)
        clear()


def inserirAresta():
    clear()
    vertice = ''
    linha = []
    while vertice != '0':
        vertice = input("Informe o elemento para inserir na matriz (digite 0 para ir a proxima):\n")
        if (vertice != '0'):
                linha.append(vertice)
    matriz.append(linha)
    clear()


def printMatriz():
    clear()
    for i in range(len(matriz)):
        print(matriz[i])


def verificarAdjacencia():
    primeiro = int(input("Selecione o primeiro vertice: ")) 
    segundo = int(input("Selecione o segundo vertice: "))
    for i in range(len(matriz[primeiro])):
        for j in range(len(matriz[segundo])):
            if (i == j):
                print("São adjacentes")
                break
    time.sleep(3)

    
def main():
    clear()
    while True:
        if (matriz == []):
            print("======================================\nMatriz ainda não gerada\n======================================")
        else:
            printMatriz()

        opcao = input("\nSelecione uma opção:\n0 - Sair\n1 - Gerar Matriz de Adjacencia\n2 - Inserir aresta\n3 - Verificar adjacencia\n\n-> ")
        if (opcao == "0"):
            clear()
            break
        if (opcao == "1"):
            listaAdjacencia()
        if (opcao == "2"):
            inserirAresta()
        if (opcao == "3"):
            if (matriz == []):
                clear()
                print("Matriz ainda não gerada")
            else:
                verificarAdjacencia()
        else:
            clear()
            print("Comando não reconhecido!")

main()
