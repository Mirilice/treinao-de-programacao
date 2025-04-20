# Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

# Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.

# Saída
# Para cada entrada, deve-se apresentar a mensagem criptografada.

casos = int(input())
for _ in range(casos):
    caso = input()
    primeira_passada = ""
    for letra in caso:
        #primeira passada
        if letra.isalpha(): #verifica se é uma letra
            letra = chr(ord(letra)+3)
            primeira_passada+=letra
        else:
            primeira_passada+=letra
    segunda_passada = primeira_passada[::-1] #inverte, como é pedido na segunda passada
    #terceira passada
    terceira_passada = ""
    metade_palavra = len(segunda_passada)//2
    for i in range(len(segunda_passada)):
        if i >= metade_palavra:
            terceira_passada+= chr(ord(segunda_passada[i])-1)
        else: terceira_passada+= segunda_passada[i]
    print(terceira_passada)
        
#chr(): converte um código Unicode ou ASCII em um caractere
#ord(): converte um caractere em ASCII