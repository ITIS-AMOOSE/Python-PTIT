from math import *

def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    temp = 0
    while (n != 0):
        temp += n % 10
        n //= 10
    return snt(temp)

def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        x = gcd(a, b)
        if check(x):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()


