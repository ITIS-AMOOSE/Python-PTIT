from math import *

N, K = map(int, input().split())

start = 10**(K - 1)
end = 10**K

result = []
for i in range(start, end):
    if gcd(i, N) == 1:
        result.append(i)
for i in range(len(result)):
    print(result[i], end = " ")
    if ((i + 1) % 10 == 0): print()