def perfect(n, f):
    if(f > 0):
        if(n % f == 0):
            vetor.append(f)
        perfect(n, f-1)
    else:
        print(vetor)

global vetor
vetor = []
perfect(10, 10)