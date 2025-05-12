T = int(input())
for i in range(T):
    sensores = input().split()
    for sensor in sensores:
        if sensores.count(sensor) == 1:
            print(sensor)
            break