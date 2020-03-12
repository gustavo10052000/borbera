def lista(l, n, i):
    try:
        if(l[i] == n): l.pop(i)
        lista(l, n, i + 1)
    except: print(">> ",l)

lista([0,1,2,3,5,2,7,1,2,3], 2, 0)