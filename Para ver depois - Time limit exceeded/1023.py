# Devido às constantes estiagens que aconteceram nos últimos tempos em algumas regiões do Brasil, o governo federal criou um órgão para a avaliação do consumo destas regiões com finalidade de verificar o comportamento da população na época de racionamento. Este órgão responsável irá pegar algumas cidades (por amostragem) e verificará como está sendo o consumo de cada uma das pessoas da cidade e o consumo médio de cada cidade por habitante.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*106), indicando a quantidade de imóveis. As N linhas contém um par de valores X (1 ≤ X ≤ 10) e Y (1 ≤ Y ≤ 200), indicando a quantidade de moradores de cada imóvel e o respectivo consumo total de cada imóvel (em m3). Com certeza, nenhuma residência consome mais do que 200 m3 por mês. O final da entrada é representado pelo número zero.

# Saída
# Para cada entrada, deve-se apresentar a mensagem “Cidade# n:”, onde n é o número da cidade seguindo a sequência (1, 2, 3, ...) e em seguida deve-se listar, por ordem ascendente de consumo, a quantidade de pessoas seguido de um hífen e o consumo destas pessoas, arredondando o valor para baixo. Na terceira linha da saída deve-se mostrar o consumo médio por pessoa da cidade, com 2 casas decimais sem arredondamento, considerando o consumo real total. Imprimir uma linha em branco entre dois casos de teste consecutivos. No fim da saída não deve haver uma linha em branco.

import math

cidade = 1
while True:
    total_pessoas = 0
    total_consumo = 0
    calculo_consumo = {}
    quant_imoveis = int(input())
    if quant_imoveis  == 0: break 
    for i in range(quant_imoveis):
        quant_moradores, consumo_total = map(int, input().split())
        media = consumo_total // quant_moradores
        if media not in calculo_consumo:
            calculo_consumo[media] = quant_moradores
        else: calculo_consumo[media] += quant_moradores
        total_consumo += consumo_total
        total_pessoas += quant_moradores
    resultado = sorted(calculo_consumo.items())
    consumo_medio = math.floor((100*total_consumo)/total_pessoas)/100
    print(f"Cidade# {cidade}:")
    print(' '.join([f"{quant_moradores}-{media}" for media, quant_moradores in resultado]))
    print(f"Consumo médio: {consumo_medio:.2f} m3.")
    print()
    cidade+=1