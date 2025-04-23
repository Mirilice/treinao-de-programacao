# In Amy's town, Sonic and his friends participate in an obstacle course to prepare for the Olympics. Four mushrooms are strategically positioned in the corners of the main square, which has the shape of a square when seen on a map. Each mushroom is located at a vertex of the main square.

# Amy is anxious to calculate the total area occupied by the main square in her beloved city. Can you help her?

# Input
# Four lines, each one containing two integers (x,y)
#  that represent the coordinates of the mushrooms (−1000≤x,y≤1000).

# It is guaranteed that the area of the square is positive and its sides are parallel to the axes of the Cartesian plane. The coordinates of the mushrooms are randomly given.

# Output
# A single integer that represents the area of the main square.

coordenadas = []
for i in range(4):
    coordenada = list(map(int, input().split()))
    coordenadas.append(coordenada)
for i in range(4):
    if coordenadas[i][0] == coordenadas[i+1][0]: #valor de x igual
        lado = abs(coordenadas[i+1][1] - coordenadas[i][1]) #subtrai o valor de y
        break
    elif coordenadas[i][1] == coordenadas[i+1][1]: #valor de y igual
        lado = abs(coordenadas[i+1][0] - coordenadas[i][0])#subtrai o valor de x
        break
print(lado**2)