# Joãozinho mora em uma rua que tem N casas. Marquinhos é o melhor amigo dele, mas sempre gosta de pregar peças em Joãozinho. Desta vez, ele pegou os dois brinquedos prediletos de Joãozinho e os escondeu em duas casas distintas da rua. Em compensação, Marquinhos deu uma dica importante para Joãozinho:

# A soma dos números das casas em que escondi teus brinquedos é igual a K. Além disso, escolhi as casas de tal forma que não existe outro par de casas cuja soma tenha esse mesmo valor.

# Sabendo disto, encontre qual é o par de casas em que se encontram os brinquedos de Joãozinho. Para auxiliar seu amigo, Marquinhos entregou a Joãozinho uma lista com o número das casas já em ordem crescente (isto é, do menor para o maior número).

# Entrada
# A primeira primeira linha da entrada contém um número inteiro N, que representa o número de casas que existem na rua. Cada uma das 
# N linhas seguintes contém um número inteiro, representando o número de uma casa. Note que esses 
# N números estão ordenados, do menor para o maior.

# A última linha da entrada contém um inteiro K, que é a soma dos números das duas casas onde os brinquedos estão escondidos.

# Saída
# Se programa deve imprimir uma única linha, contendo dois inteiros, 
# A e B, A < B, que representam os números das casas em que estão escondidos os brinquedos. Os dois números devem ser separados por um espaço em branco.

quant_casas = int(input())
casas = []
valores = set() #evita TLE, porque o set é mais rápido para verificar se um item existe
for i in range(quant_casas):
    casa = int(input())
    casas.append(casa)
    valores.add(casa)
soma = int(input())
for casa1 in casas:
    casa2 = soma - casa1
    if casa2 in valores and (casa1 != casa2):
        print(casa1, casa2)
        break
