n, budget = [int(el) for el in input().split()]
values = [int(el) for el in input().split()]
prices = [int(el) for el in input().split()]

pairs = [(val, price) for val, price in zip(values, prices)]

pairs = list(sorted(pairs, key=lambda x: x[0]))

res = pairs[0][0]

for i in range(n):
    budget -= pairs[i][1]
    if (budget < 0) or (i == n-1):
        res = pairs[i][0]
        break


print(res)
