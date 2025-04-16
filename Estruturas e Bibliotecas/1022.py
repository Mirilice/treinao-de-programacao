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
