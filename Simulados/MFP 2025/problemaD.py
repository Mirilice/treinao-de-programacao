#com ajuda do monitor:
# pi = 3.14159265359
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
#     resultado = float('inf')
#     for r in R:
#         caminho = abs(r1 - r) + abs(r2 - r) + (2 * pi * r * dlinha / N)
#         resultado = min(resultado, caminho)
#     print(f"{resultado:.10f}")