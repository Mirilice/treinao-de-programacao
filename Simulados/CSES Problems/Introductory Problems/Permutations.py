n = int(input())
if n == 3 or n == 2:
    print("NO SOLUTION")
else:
    par = [i for i in range(2, n+1, 2)]
    impar = [i for i in range(1, n+1, 2)]
    total = par + impar
    print(*total)