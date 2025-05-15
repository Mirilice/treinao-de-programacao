# Monocarp decided to embark on a long hiking journey.

# He decided that on the first day he would walk a kilometers, on the second day he would walk b kilometers, on the third day he would walk c kilometers, on the fourth day, just like on the first, he would walk a kilometers, on the fifth day, just like on the second, he would walk b kilometers, on the sixth day, just like on the third, he would walk c kilometers, and so on.

# Monocarp will complete his journey on the day when he has walked at least n kilometers in total. Your task is to determine the day on which Monocarp will complete his journey.

# Input
# The first line contains one integer t (1≤t≤104) — the number of test cases.

# Each test case consists of one line containing four integers n, a, b, c (1≤n≤109; 1≤a,b,c≤106).

# Output
# For each test case, output one integer — the day on which Monocarp will have walked at least n kilometers in total and will complete his journey.

casos = int(input())
for _ in range(casos):
    meta, a, b, c = map(int, input().split())
    vetor = []
    vetor.append(a)
    vetor.append(b)
    vetor.append(c)
    total = 0
    dias = 0
    prefix = [0]*len(vetor)
    for i in range(len(vetor)):
        prefix[i] = prefix[i-1] + vetor[i]
    # print(prefix)
    
    while total < meta:
        if prefix[2] >= meta:
            for i in range(len(prefix)):
                if prefix[i] >= meta:
                    dias = i + 1 
                    total = prefix[i]
                    break
        else:
            voltas = meta // prefix[2]
            dias = voltas*3
            total = voltas*prefix[2]
            resto = meta % prefix[2]
            if resto:
                for i in range(len(prefix)):
                    if prefix[i] >= resto:
                        dias += (i + 1) 
                        total += prefix[i]
                        break
    print(dias)