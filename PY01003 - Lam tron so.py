t = int(input())

while t:
    n = int(input())
    mul = 10
    while n >= mul:
        du = n % mul
        if du >= mul // 2:
            n += mul - du
        else:
            n -= du
        mul *= 10
    print(n)
    t -= 1