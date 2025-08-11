def solve(a):
    ans = ""
    i = 0
    while i < len(a):
        char = a[i]
        cnt = int(a[i + 1])
        ans += char * cnt
        i += 2
    return ans


t = int(input())

for _ in range(t):
    a = input()
    print(solve(a))