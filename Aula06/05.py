def lista(l, n):
    if(n in l):
        l.remove(n)
        lista(l, n)
    return(l)

print(lista([0,1,2,2,2,2,2,3,5,2,7,1,2,3], 2))