from math import *

t = int(input())

for _ in range(t):
    n = input()
    n2 = n[::-1]
    if gcd(int(n), int(n2)) == 1:
        print("YES")
    else:
        print("NO")