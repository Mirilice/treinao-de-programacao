# Ogros marcianos, como todos sabem, são extremamente fortes.

# Numa feira de circo marciano, ogros são chamados para bater um martelo num aparelho que mede sua força. O ogro ganha um determinado prêmio dependendo da faixa de força que alcançou (por exemplo, se a força alcançada foi entre 0 e 5, ganha 10 pontos. Se for entre 6 e 10, ganha 30). São possíveis 
# N premiações, para N faixas de força alcançadas.

# Você deve escrever um programa que recebe quais são as faixas de forças e suas respectivas premiações. Em seguida, o programa recebe a força alcançada por 
# M ogros, e deve calcular quanto cada ogro recebeu de premiação.

# Entrada
# A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).

# A primeira linha contém dois inteiros 
# N e M, representando respectivamente o número de faixas de premiações e o número de ogros cuja força foi medida.

# A segunda linha de um caso de teste contém 
# N−1 inteiros Ai. A primeira faixa de premiação é dada por forças menores que 
# A1. A i-ésima faixa de premiação é composta das forças que são maiores ou iguais a 
# Ai−1 e menores que Ai. A n-ésima pontuação é composta das forças maiores ou iguais a 
# AN−1.

# A terceira linha contém N inteiros Fi em ordem crescente, representando a premiação de cada faixa de premiação, nesta ordem.

# A quarta e última linha de um caso de teste contém M inteiros Oi, um para cada ogro, representando qual força cada ogro alcançou.

# Saída
# Seu programa deve imprimir, na saída padrão, uma única linha, contendo 
# M inteiros, um para cada ogro, na ordem dada pela entrada, representando qual premiação cada ogro recebeu pela sua força alcançada.

N, quant_ogros = map(int, input().split())
forcas = list(map(int, input().split()))
premiacao = list(map(int, input().split()))
ogros = list(map(int, input().split()))
resultado = []
def busca_ogros():
    inicio = 0
    fim = len(forcas)
    while inicio < fim:
        mid = (inicio+fim)//2
        if forcas[mid] <= p:
            inicio = mid + 1 
        else: fim = mid
    return inicio
for p in ogros:
    index = busca_ogros()
    resultado.append(premiacao[index])
print(*resultado)