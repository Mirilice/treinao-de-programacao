# Faça um programa para ler dois inteiros X e Y representando um ponto em um plano cartesiano. Imprima qual quadrante esse ponto de encontra. Caso o ponto esteja em algum eixo, imprima apenas a mensagem "eixos".

# Entrada
# A entrada consiste de duas linhas. A primeira linha contém o inteiro X. A segunda linha contém o inteiro Y.

# Saída
# A saída consiste de uma linha contendo a mensagem indicando qual o quadrante que o ponto está.

X = int(input())
Y = int(input())

if X == 0 or Y == 0: print("eixos")
elif X > 0 and Y > 0: print("Q1")
elif X < 0 and Y > 0: print("Q2")
elif X < 0 and Y < 0: print("Q3")   
elif X > 0 and Y < 0: print("Q4")