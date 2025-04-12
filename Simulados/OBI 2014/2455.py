

P1, C1, P2, C2 = map(int, input().split())
diferenca = P1*C1 - P2*C2
if diferenca == 0:
    print("0")
elif diferenca < 0: print("1")
else: print("-1")