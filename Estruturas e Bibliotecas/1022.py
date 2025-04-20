# A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

# Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
# Soma: (N1*D2 + N2*D1) / (D1*D2)
# Subtração: (N1*D2 - N2*D1) / (D1*D2)
# Multiplicação: (N1*N2) / (D1*D2)
# Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

# Entrada
# A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

# Saída
# A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.

casos =  int(input())
for _ in range(casos):    
    operacao = input().split()
    N1 = int(operacao[0])
    N2 = int(operacao[4])
    D1 = int(operacao[2])
    D2 = int(operacao[6])
    sinal = operacao[3]
    def soma():
        numerador = N1*D2 + N2*D1
        denominador = D1*D2
        return numerador, denominador
    def sub():
        numerador = N1*D2 - N2*D1
        denominador = D1*D2
        return numerador, denominador
    def mult():
        numerador = N1*N2
        denominador = D1*D2
        return numerador, denominador
    def div():
        numerador = N1*D2
        denominador = N2*D1
        return numerador, denominador
    if sinal == "+":
        numerador, denominador = soma()
    elif sinal == "-":
        numerador, denominador = sub()
    elif sinal == "*":
        numerador, denominador = mult()
    else: numerador, denominador = div()
    def mdc(numerador, denominador):
        while denominador !=0:
            resto = numerador % denominador
            numerador = denominador
            denominador = resto
        return numerador
    mdc = mdc(numerador, denominador)
    novo_numerador = numerador//mdc
    novo_denominador = denominador//mdc
    print(f"{numerador}/{denominador} = {novo_numerador}/{novo_denominador}")
