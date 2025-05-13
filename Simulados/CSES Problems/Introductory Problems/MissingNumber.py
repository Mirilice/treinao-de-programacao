n = int(input())
lista = list(map(int, input().split()))
soma = n*(n+1)//2
soma_atual = sum(lista)
print(soma-soma_atual)