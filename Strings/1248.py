# O doutor deu a você a sua dieta, na qual cada caractere corresponde a algum alimento que você deveria comer. Você também sabe o que você tem comido no café da manha e no almoço, nos quais cada caractere corresponde a um tipo de alimento que você deveria ter comido aquele dia. Você decidiu que irá comer todo o restante de sua dieta durante o jantar, e você quer imprimi-la como uma String (ordenada em ordem alfabética). Se você trapaceou de algum modo (ou por comer muito de tipo de alimento, ou por comer algum alimento que não está no plano de dieta), você deveria imprimir a cadeia "CHEATER" (significa trapaceiro), sem as aspas.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste é composto por três linhas, cada uma delas com uma string com até 26 caracteres de 'A'-'Z' ou vazia, representando respectivamente os alimentos da dieta, do café da manhã e do almoço.

# Saída
# Para cada caso de teste imprima uma string que representa os alimentos que você deveria consumir no jantar, ou "CHEATER" caso você tenha trapaceado na sua dieta.

casos = int(input())
for _ in range(casos):
    dieta = input()
    cafe = input()
    almoco = input()
    comida = cafe+almoco
    cheater = False
    for i in range(len(comida)):
        if comida[i] not in dieta:
            cheater = True
            break
        else:
            dieta = dieta.replace(comida[i], '')
    if cheater:
        print("CHEATER")
    else:
        dieta = sorted(dieta) #nao pode usar sort() em string
        dieta = ''.join(dieta)
        print(dieta)