from math import *

def nguyento(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1 , n + 1):
        if gcd(i, n) == 1:
            cnt += 1
    if(nguyento(cnt)):
        print("YES")
    else:
        print("NO")