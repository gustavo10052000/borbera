def significativo(n, i):
    if(str(n)[i] == 0 or str(n)[i] == '.'):
        significativo(n, i+1)
    else:
        print(str(n)[i])

significativo(00.03456, 0)