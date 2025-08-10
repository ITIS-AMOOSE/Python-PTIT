t = int(input())

for _ in range(t):
    n = str(input())

    ok = True
    for i in range(len(n) - 1):
        if (n[i] > n[i + 1]):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")