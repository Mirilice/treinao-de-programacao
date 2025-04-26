# Em todo universo existe uma constante mística que rege e coordena todos os eventos (por exemplo, no
# nosso universo esta constante é o 42). Em estudos recentes, Amy encontrou uma relação de forças entre
# moedas e acha que está muito perto de encontrar a constante mística do universo e do mundo para o
# universo Sonic! No entanto, existe uma superstição de que, se essa constante é negativa, o universo é
# condenado a falência, se for nula, o universo não evoluirá e se for positiva, o universo será próspero e feliz.
# A relação encontrada por Amy foi a seguinte:
# onde M1 e M2 são propriedades específicas das moedas e D é a distância entre elas. Nesse caso G é a
# constante mística do universo e do mundo e F é a força de atração entre as moedas.
# ‌Dados os valores de M1, M2, X1, X2 e F, sendo: M1 e M2 as propriedades, X1 e X2 as posições das
# moedas e F a força entre elas, calcule G o valor de G para ajudar Amy a descobrir o futuro do universo.
# Input
# A primeira linha da entrada contém os valores de M1 e M2.
# A segunda linha contém os valores de X1 e X2.
# A terceira e última linha contém o valor de F.
# Output
# Imprima em uma única linha o valor de G definido no enunciado. Sua resposta será considerada correta
# se o erro absoluto ou o erro relativo forem menores que 10^−6.
# Para python você pode usar a função round:
# print(round(G,10)), para ter 10 casas, por exemplo.
# Para C++, use:
# cout « setprecision(10) « fixed « G « endl;

M1, M2 = map(float, input().split())
X1, X2 = map(float, input().split())
F = float(input())
D = X2 - X1
G = (F*(D**2))/(M1*M2)
print(round(G,10))