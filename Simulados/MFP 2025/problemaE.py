#depois da explicação do monitor
N, M = map(int, input().split())
matriz = []
for i in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(N):
    for j in range(M):
        valor = i + j 
        if valor % 2 == 0:
            if matriz[i][j]  % 2 != 0:
                matriz[i][j] +=1 
        else:
            if matriz[i][j] % 2== 0:
                matriz[i][j] += 1
                
for i in range(N):
    for j in range(M):
        print(matriz[i][j], end=" ")
    print()
    