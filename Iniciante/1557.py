# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

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