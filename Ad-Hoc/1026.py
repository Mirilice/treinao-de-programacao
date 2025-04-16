while True:
    try:
        num1, num2 = map(int, input().split())
        print(num1 ^ num2) #XOR (Exclusive OR)
    except EOFError:
        break