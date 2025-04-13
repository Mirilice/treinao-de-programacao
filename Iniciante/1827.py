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