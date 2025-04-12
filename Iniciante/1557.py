while True:
    n = int(input())
    if n == 0: break
    T = len(str(2**(2*(n-1)))) #valor para espaçamento pedido na questão (dígitos do maior número da matriz)
    for i in range(n):
        for j in range(n):
            valor = 2**(i+j)
            if j == 0:
                print(f'{valor:>{T}}', end="")
            else: print(f' {valor:>{T}}', end="")
            # onde:
            # : indica que você quer formatar esse valor.
            # > significa que o valor deve ser alinhado à direita.
            # {T} largura total do campo (pedido pela questão)
        print() #quebra de linha 
    print() #espaço entre matrizes