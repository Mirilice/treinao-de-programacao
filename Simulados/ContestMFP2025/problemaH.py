# Allen has a LOT of money. He has n dollars in the bank. For security reasons, he wants to withdraw it in cash (we will not disclose the reasons here). The denominations for dollar bills are 1, 5, 10, 20, 100. What is the minimum number of bills Allen could receive after withdrawing his entire balance?

# Input
# The first and only line of input contains a single integer n(1≤n≤109).

# Output
# Output the minimum number of bills that Allen could receive.

n = int(input())
cem = n // 100
resto = n % 100
vinte = resto // 20
resto = resto % 20
dez = resto // 10
resto = resto % 10
cinco = resto // 5
resto = resto % 5
um = resto
print(cem + vinte + dez + cinco + um)