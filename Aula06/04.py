def significativo(n, i):
    if(str(n)[i] == 0):
        significativo(n, i+1)
    else:
        print(str(n)[i])

significativo(3456, 0)