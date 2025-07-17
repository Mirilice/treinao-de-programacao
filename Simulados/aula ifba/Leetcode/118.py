class Solution(object):
    def generate(self, numRows):
        lista = []
        for i in range(numRows):
            if i == 0:
                lista.append([1])
            elif i == 1:
                lista.append([1,1])
            else:
                numbers = []
                for j in range(i+1): 
                    if j == 0 or j == i:
                        numbers.append(1)
                    else:
                        number = (lista[i-1][j-1]) + (lista[i-1][j])
                        numbers.append(number)
                lista.append(numbers)
        return lista
        