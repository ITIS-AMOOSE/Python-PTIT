def Phan_tich_thua_so_nguyen_to(n):
    if n < 2:
        return []   
    phan_tich = []
    for i in range(2, n + 1):
        while n % i == 0:
            phan_tich.append(i)
            n //= i
    return phan_tich


t = int(input())

for _ in range (t):
    n = int(input())
    a = Phan_tich_thua_so_nguyen_to(n)
    if not a:
        print("1")
        continue
    result = ["1"]
    cnt = 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            result.append(f"{a[i]}^{cnt}")
            cnt = 1
    result.append(f"{a[-1]}^{cnt}")
    print(" * ".join(result))
