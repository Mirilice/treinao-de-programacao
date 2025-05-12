#grafos
quant_pontos, quant_ruas = map(int, input().split())
adjs = [[] for _ in range(quant_pontos+1)]
visitados = [False] * (quant_pontos+1)
for _ in range(quant_ruas):
    a, b = map(int, input().split())
    adjs[a].append(b)
    adjs[b].append(a)
pilha = []
componentes = 0
for i in range(1, quant_pontos+1):
    if not visitados[i]:
        componentes += 1
        pilha.append(i)
        while pilha:
            u = pilha.pop()
            if not visitados[u]:
                visitados[u] = True
                for v in adjs[u]:
                    if not visitados[v]:
                        pilha.append(v)
if componentes == 1 and quant_ruas == quant_pontos - 1:
    print("BOM")
else:
    ruas_destruir = quant_ruas - (quant_pontos - componentes)
    ruas_construir = componentes - 1
    print("RUIM", ruas_destruir, ruas_construir)