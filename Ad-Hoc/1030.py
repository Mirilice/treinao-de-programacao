casos = int(input())
for i in range(casos):
    n, passo= map(int, input().split())
    lista = [i for i in range(1, n+1)]
    indice = 0
    while True:
        if len(lista) == 1: break
        indice = (indice + passo -1)%len(lista)
        lista.pop(indice)
    print(f"Case {i+1}: {lista[0]}")