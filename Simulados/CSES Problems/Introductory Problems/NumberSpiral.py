casos = int(input())
for _ in range(casos):
    l,c = map(int, input().split())
    basec = c + (c-1)**2
    basel = l + (l-1)**2
    #diagonal principal
    if l == c:
        print(basec)
    #linha maior que a coluna
    elif l > c:
        if l % 2 == 0: #se a linha for par
            print(basel + (l-c))
        else: print(basel - (l-c))
    else:
        if c % 2 == 0:
            print(basec - (c-l))
        else:
            print(basec + (c-l))
    