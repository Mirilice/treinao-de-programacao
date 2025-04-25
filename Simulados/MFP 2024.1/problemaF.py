#programacao - 8 
#volei - 4
#futebol - 2
#corrida - 1 
total_esportes = 0
pontos = int(input())
i = 3
while pontos > 0:
    if pontos - 2**i >= 0:
        pontos -= 2**i
        total_esportes += 1
    i-=1
print(total_esportes)