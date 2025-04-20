# Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

# Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

# Entrada
# A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

# Saída
# Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de teste, imprima uma linha em branco.

try:
    #primeiro rodar 2,3,0, elementos externos da matriz depois 1,4 
    while True:
        n = int(input())
        #gerando a matriz
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        # preenchendo a matriz corretamente:
        for i in range(n):
            for j in range(n):
                #diagonal principla
                if (i == j): matriz[i][j] = 2
                #diagonal secundária
                elif (i + j == n-1): matriz[i][j] = 3
        inicio = n//3 #a questão fornece isso
        fim = n - inicio
        
        for i in range(inicio, fim):
            for j in range(inicio, fim):
                matriz[i][j] = 1
                
        matriz[n//2][n//2] = 4
        
        #escreve a matriz
        for i in range(n):
            for j in range(n):
                print(matriz[i][j], end="")
            print()
        print() #espaço entre as matrizes
        
except EOFError:
    pass