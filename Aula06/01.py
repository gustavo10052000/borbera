def multiplication(x, y, z):
    if (y != 0):
        multiplication(x, y - 1, x + z)
    else:
        print(z)

multiplication(4, 11, 0)