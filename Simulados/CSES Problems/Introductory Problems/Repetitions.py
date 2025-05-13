dna = input()
current = 1
maxim = 1
for i in range(1, len(dna)):
    if dna[i] == dna[i-1]:
        current += 1
    else: 
        maxim = max(maxim, current)
        current = 1
maxim = max(maxim, current)
print(maxim)