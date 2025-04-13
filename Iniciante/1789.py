try:
    while True:
        L = int(input())
        lesmas = list(map(int, input().split()))
        lesma_veloz = max(lesmas)
        if lesma_veloz < 10: print("1")
        elif lesma_veloz >= 20: print("3")
        else: print("2")
except EOFError:
    pass
