# Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

# Primeiro os Pares
# Depois os Ímpares
# Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

# Entrada
# A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

# Saída
# Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.

numeros = int(input())
pares = []
impares = []
for _ in range(numeros):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
    else: impares.append(n)
pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    print(pares[i])
for i in range(len(impares)):
    print(impares[i])