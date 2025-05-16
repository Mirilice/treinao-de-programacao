# The store sells n items, the price of the i-th item is pi. The store's management is going to hold a promotion: if a customer purchases at least x items, y cheapest of them are free.

# The management has not yet decided on the exact values of x and y. Therefore, they ask you to process q queries: for the given values of x and y, determine the maximum total value of items received for free, if a customer makes one purchase.

# Note that all queries are independent; they don't affect the store's stock.

# Input
# The first line contains two integers n and q (1≤n,q≤2⋅105) — the number of items in the store and the number of queries, respectively.

# The second line contains n integers p1,p2,…,pn (1≤pi≤106), where pi — the price of the i-th item.

# The following q lines contain two integers xi and yi each (1≤yi≤xi≤n) — the values of the parameters x and y in the i-th query.

# Output
# For each query, print a single integer — the maximum total value of items received for free for one purchase.

n, query = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort(reverse=True)
prefix = [0]*n
prefix[0] = prices[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + prices[i]
for _ in range(query):
    products, free = map(int, input().split())
    if free == products:
        print(prefix[products - 1])
    else:
        print(prefix[products - 1] - prefix[products - free - 1])
