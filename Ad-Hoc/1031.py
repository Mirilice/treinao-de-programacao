while True:
    n = int(input())
    if n == 0: break
    salto = 1 #salto mínimo
    #problema matemático de flavio josefo
    while True:
        regioes = [i for i in range(1,n+1)]
        indice = 0
        regioes.pop(0) #a região 1 precisa ser desligada primeiro
        while len(regioes) > 1: 
            indice = (indice + salto -1) % len(regioes)
            regioes.pop(indice)
        if regioes[0] == 13: #regiao que queremos por último
            print(salto)
            break
        salto+=1
        
        
    