# Blocos de Madeira é um jogo onde você recebe peças de madeira que vêm em oito formas, conforme mostrado abaixo:

# beecrowd

# O objetivo do jogo é montar o retângulo mais largo que pode ser feito de um subconjunto das peças dadas com as seguintes condições:

# O retângulo deve ter bordas lisas. Em outras palavras, a peça mais à esquerda deve ser (peça nº 1) e a peça mais à direita deve ser (peça nº 2).
# As peças adjacentes devem se encaixar corretamente. Por exemplo, a peça #4 ou a peça #5 devem aparecer à direita da peça #1. Da mesma forma, a peça #4 pode aparecer à direita da peça #1 ou da peça #3.
# Nenhuma peça se encaixa à esquerda da peça #1. Nenhuma peça se encaixa à direita da peça #2.
# Para cada peça #1, o retângulo deve ter uma peça #2 correspondente. Da mesma forma, para cada peça #5, deve haver uma peça #6 correspondente./li>
# Por exemplo, os dois exemplos a seguir são arranjos válidos:

# beecrowd

# Considerando que os três seguintes não são:

# beecrowd

# Uma empresa de informática está interessada em construir um videogame dos Blocos de Madeira e contratou você para escrever um programa que determina se a disposição de uma determinada peça é válida de acordo com as regras acima ou não.

# Entrada
# Seu programa será testado em um ou mais casos de teste. Cada caso de teste é especificado em uma linha de entrada separada. Cada peça é especificada usando o dígito associado a ela como na figura anterior. Um arranjo é especificado listando seus dígitos sem espaços entre os dígitos. Cada arranjo terá pelo menos uma peça, mas não mais que 10.000 peças.
# A última linha no arquivo de entrada terá um único 0. Essa linha não faz parte dos casos de teste.

# Saída
# Para cada caso de teste, imprima o resultado em uma única linha usando o seguinte formato:
# k._resultado
# Onde k é o número do caso de teste (começando em 1) e o resultado é "VALID" se o arranjo for válido, ou "NOT" se não for.

prox_encaixe = {
    '1': ['4','5'],
    '3': ['4','5'],
    '4': ['2','3'],
    '5': ['8'],
    '6': ['2','3'],
    '7': ['8'],
    '8': ['6','7']
}
caso = 1
while True:
    valid = True
    peca = input()
    if peca == '0': break
    if peca[0] != '1' or peca[-1] != '2':
        valid = False
    for i in range(len(peca) - 1): #pro loop não ultrapassar o tamanho da string
        atual = peca[i]
        prox = peca[i+1]
        if prox not in prox_encaixe.get(atual, []):
            #get(chave, valor_padrao)
            valid = False
    #ultimo caso: a quantidade de pecas1 = pecas2 e pecas5=pecas6
    if peca.count('1') != peca.count('2') or peca.count('5') != peca.count('6'): valid = False
    if (valid): print(f"{caso}. VALID")
    else: print(f"{caso}. NOT")
    caso+=1