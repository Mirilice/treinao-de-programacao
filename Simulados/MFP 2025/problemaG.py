palavra = input()
A = ""
B = ""
for i in range(len(palavra)):
    if i % 2 == 0:
        A += palavra[i]
    else: B+= palavra[i]
print(A)
print(B)