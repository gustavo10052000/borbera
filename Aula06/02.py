def pow(x, y):
    if (y != 0):
        pow(x + x, y - 1)
    else:
        print(x)

pow(2, 10)