# Nlogonia é conhecida por sua indústria de tradicionais tapetes quadrados, que são produzidos apenas com dimensões inteiras, para todos os números inteiros positivos. Quer dizer, os tapetes são de dimensão 1 × 1, 2 × 2, 3 × 3, e assim por diante. João Tapetão, grande empresário do setor, está planejando o próximo carregamento para exportação, que deve ser de exatamente N tapetes. Os tapetes são sempre enrolados e colocados em um tubo, um após o outro. Por exemplo, para um carregamento de N = 4 tapetes de dimensões 2 × 2, 4 × 4, 6 × 6 e 3 × 3, será necessário um tubo de comprimento 2 + 4 + 6 + 3 = 15. A questão é que o preço do tapete é proporcional à sua área, de modo que quanto maior a soma das áreas dos tapetes, maior o lucro do Tapetão. No exemplo anterior, a soma das áreas é 22 + 42 + 62 + 32 = 65. Só que daria para lucrar mais, com o mesmo tubo de comprimento 15, se o carregamento fosse com quatro tapetes de dimensões 1 × 1, 4 × 4, 7 × 7 e 3 × 3, cuja soma das áreas dá 75. Será que daria para lucrar ainda mais?

# O navio chegou e Tapetão precisa embarcar o carregamento. Há apenas um tubo de comprimento L e o carregamento deve conter exatamente N tapetes. Qual é a maior soma possível das áreas dos N tapetes que poderá ser transportada?

# Entrada
# A primeira e única linha da entrada contém dois inteiros, L e N (N ≤ L, 1 ≤ L ≤ 106 e 1 ≤ N ≤ 105), o comprimento do tubo e a quantidade de tapetes que deve transportada, respectivamente.

# Saída
# Seu programa deve produzir uma única linha, contendo apenas um inteiro, a maior soma possível das áreas dos tapetes.

#exemplo com 10 (L) e 5(N):
#maximiza um tapete, entao vai ficar 4 de 1m^2 (N-1 -> tapetes_pequenos)
#o resto vai ficar 10-4 = 6 (L - tapetes_pequenos -> tapete_maior)
# total vai ser 6*6 = 36 + tapetes_pequenos = 40 (tapete_maior**2 + tapetes_pequenos)
L, N = map(int, input().split())
tapetes_pequenos = N - 1 
tapete_maior = L - tapetes_pequenos
area = (tapete_maior**2 + tapetes_pequenos)
print(area)
# muito interessante esse exercício, pois:
# Para maximizar a soma das áreas com comprimento fixo, concentre o valor em um único lado
# Os outros lados devem ser os menores possíveis (1), para deixar mais espaço pro tapete grandão