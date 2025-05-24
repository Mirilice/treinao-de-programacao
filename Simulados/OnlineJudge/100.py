itens = {}
while True:
    try:
        i, j = map(int, input().split())
        valor_max = max(i,j)
        valor_min = min(i,j)
        maxcycle = 0
        cycle = 0
        for n in range(valor_min, valor_max+1):
            n_inicial = n
            while n >= 1:
                # print(n)
                if n in itens:
                    # print("tem n no dicionario")
                    cycle += itens[n]
                    break
                cycle += 1
                if n == 1: break
                # print(n, end=" ")
                if n % 2 != 0:
                    n = 3*n + 1
                else: n = n//2
            itens[n_inicial] = cycle
            maxcycle = max(maxcycle, cycle)
            cycle = 0
        print(f"{i} {j} {maxcycle}")
    except EOFError:
        break
