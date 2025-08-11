def solve(a):
    ans = ""
    cnt = 1
    for i in range (1, len(a)):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            ans += str(cnt) + a[i - 1]
            cnt = 1
    ans += str(cnt) + a[-1]
    return ans

t = int(input())

for _ in range(t):
    a = input()
    print(solve(a))