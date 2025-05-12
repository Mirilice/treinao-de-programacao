#duvida de como fazer com que conte a partir da criança escolhida
criancas = int(input())
escolhida = int(input())
pato = int(input())
seletores_criancas = [i for i in range(1, criancas+1)]
seletores_criancas.remove(escolhida)
proxima = (escolhida % criancas) + 1
if proxima in seletores_criancas:
    i = seletores_criancas.index(proxima)
else:
    i = 0
for _ in range(pato):
    i = (i + 1) % len(seletores_criancas)
print(seletores_criancas[i])