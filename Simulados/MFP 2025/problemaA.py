#inicio com duvida na explicacao - inicialmente deu TLE
quant_medida, amplitude = map(int, input().split())
minutos = list(map(int, input().split()))
freq = [0] * (amplitude + 2) 
for minuto in minutos:
    freq[minuto] += 1
for i in range(amplitude, 0, -1):
    freq[i] += freq[i+1]
for i in range(1, amplitude+1):
    print(freq[i], end=" ")