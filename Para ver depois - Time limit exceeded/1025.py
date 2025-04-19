case = 1
while True:   
    pedras, consultas = (map(int, input().split()))
    if pedras == 0 and pedras == consultas: break
    marmores = []
    total_consultas = []
    for _ in range(pedras):
        pedra = int(input())
        marmores.append(pedra)
    for _ in range(consultas):
        consulta = int(input())
        total_consultas.append(consulta)
    marmores.sort()
    print(f"CASE# {case}:")
    for i in range(len(total_consultas)):
        if total_consultas[i] in marmores:
            print(f"{total_consultas[i]} found at {marmores.index(total_consultas[i])+1}")
        else: print(f"{total_consultas[i]} not found")
    case+=1
        