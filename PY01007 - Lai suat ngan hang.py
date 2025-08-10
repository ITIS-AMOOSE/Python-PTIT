t = int(input())

for _ in range(t):
    N, X, M = map(float, input().split())
    cnt = 0
    while N < M:
        N += N/100 * X
        cnt += 1
    print(cnt)