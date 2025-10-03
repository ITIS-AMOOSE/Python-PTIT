def Tong_chu_so(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def Kiem_tra_chu_so(n):
    for i in range(len(n) - 1):
        if (abs(int(n[i]) - int(n[i + 1])) != 2):
            return False
    return True

t = int(input())

for _ in range(t):
    n = input().strip()
    sum_chu_so = Tong_chu_so(int(n))
    if sum_chu_so % 10 == 0 and Kiem_tra_chu_so(n):
        print("YES")
    else:
        print("NO")