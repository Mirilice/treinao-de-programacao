# Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.

# Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

# Entrada
# A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

# Saída
# Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo.

A,B,C,D = map(int, input().split())
def triangulo(a,b,c):
    return a+c>b and b+a>c and b+c>a #condição de existência do triângulo
resposta = triangulo(A,B,C) or triangulo(A,B,D) or triangulo(A,C,D) or triangulo(B,C,D) #todas possibilidades de lados do triângulo
if resposta: print("S")
else: print("N")