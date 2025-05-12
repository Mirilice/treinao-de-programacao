# import math

# R = list(map(int, input().split()))
# N, Q = map(int, input().split())

# for _ in range(Q):
#     C1, L1, C2, L2 = map(int, input().split())
#     C1 -= 1
#     L1 -= 1
#     C2 -= 1
#     L2 -= 1
#     r1 = R[C1]
#     r2 = R[C2]
#     dist_radial = abs(r1 - r2)
#     dlinha = abs(L1 - L2)
#     dlinha = min(dlinha, N - dlinha)
#     circ1 = 2 * math.pi * r1
#     circ2 = 2 * math.pi * r2
#     caminho1 = (circ1 * dlinha / N) + dist_radial
#     caminho2 = (circ2 * dlinha / N) + dist_radial
#     resultado = min(caminho1, caminho2)
#     print(f"{resultado:.9f}")