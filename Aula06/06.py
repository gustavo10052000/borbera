def perfect(m):
    if(m > 0):
        if(n % m == 0 ):
            vetor.append(m)
        perfect(m-1)
    print(vetor)
    exit()


global n, vetor
n = 6
vetor = []
perfect(n)