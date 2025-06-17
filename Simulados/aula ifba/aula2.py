melhores_precos = {1:1, 2:5, 3:8, 4:10, 5:13, 6:17, 7:18, 8:22, 9:25, 10:30}

receita = 0
while True:
    comprimento_barra = int(input())
    if comprimento_barra == -1: break
    mid = (comprimento_barra//2) - 1
    for i in range(comprimento_barra, mid, -1):
        if comprimento_barra in melhores_precos:
            receita = melhores_precos[comprimento_barra]
            break
        indice = comprimento_barra-i
        if i in melhores_precos and indice in melhores_precos:
            valor = melhores_precos[i] + melhores_precos[indice]
            print(i, indice, melhores_precos[i], melhores_precos[indice])
            receita = max(receita, valor)
    print(f"Receita: R${receita},00")
    melhores_precos[comprimento_barra] = receita
print(melhores_precos)
#precisa de ajuste