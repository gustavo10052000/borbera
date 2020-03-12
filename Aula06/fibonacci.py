def fibonacci(n, m):
    print(m)
    if (m < limite):
        m = n + m
        n = m - n
        fibonacci(n, m)
    else:
        exit()


global limite
limite = int(input("Informe o valor maximo que deseja alcançar: "))
fibonacci(n = 1, m = 1)