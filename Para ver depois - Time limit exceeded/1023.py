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