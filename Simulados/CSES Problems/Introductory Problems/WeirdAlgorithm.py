# Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. 
# Your task is to simulate the execution of the algorithm for a given value of n.
# Input
# The only input line contains an integer n.
# Output
# Print a line that contains all values of n during the algorithm.

# Example
# Input:
# 3

# Output:
# 3 10 5 16 8 4 2 1

n = int(input())
print(n, end=" ")
while n != 1:
    if n % 2 == 0:
        n /= 2
        print(int(n), end=" ")
    else: 
        n = n*3 + 1
        print(int(n), end=" ")
        