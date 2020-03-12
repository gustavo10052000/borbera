def primos(m, n):
    if (len(divisores) > 2):
        m = 0

    if (m != 0):
        if (n % m == 0):
            divisores.append(m)
        primos(m-1, n)

    if (divisores != []):
        if(len(divisores) == 2):
            qntPrimos.append(n)
            print(divisores)
        divisores.clear()
        primos(n-1, n-1)

    return (len(qntPrimos))

divisores = []
qntPrimos = []
n = 40
print(primos(n, n))
