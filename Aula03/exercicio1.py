import os

length = int(input("Insira o numero de vértices do grafo:\n"))
matriz = []
os.system('cls')

for i in range(length):
    matriz.append([])
    firstValue = 0
    value = ''
    while (value != "next"):
        if (firstValue == 0):
            value = input("Insira o nome do vértice\n(Digite 'next' para ir a proxima aresta):\n")
            firstValue += 1
        else:
            value = input("Insira os vértices adjacentes ao vértice "+str(matriz[i][0])+"\n(Digite 'next' para ir a proxima aresta)\n")

        if (value != "next"):
            matriz[i].append(value)
        
        os.system('cls')

for i in range(len(matriz)):
    grau = int(len(matriz[i])) - 1
    print(str(matriz[i])+", grau: "+str(grau))