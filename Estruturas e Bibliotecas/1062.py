while True:
    try:
        vagoes = int(input())
        if vagoes == 0: break
        while True:
            A = list(map(int, input().split()))
            B = [i for i in range(1, vagoes+1)]
            if B[0] == 0: break
            estacao = []
            # print(A)
            # print(B)
                
            while len(A)> 0 or len(B)>0 or len(estacao)>0:
                if len(A)>0 and len(B)>0 and A[-1] == B[-1]:
                    A.pop()
                    B.pop()
                elif len(estacao)>0 and len(B)>0 and estacao[-1] == B[-1]:
                    estacao.pop()
                    B.pop()
                elif len(A) > 0:
                    estacao.append(A.pop())
                else: break
            if len(A) == 0 and len(B) == 0 and len(estacao) == 0:
                print("Yes")
            else: print("No")
        print()
    except EOFError:
        break
        