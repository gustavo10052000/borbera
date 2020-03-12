def perfect(m):
    if(m > 0):
        if(n % m == 0 and m != n): vetor.append(m)
        perfect(m-1)
    if(sum(vetor) == n): return True
    return False

global n
n = 24
vetor = []
print(perfect(n))