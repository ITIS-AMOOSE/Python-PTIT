a, K, N = map(int, input().split())

ok = False
first_b = K - (a % K) if a % K != 0 else K

for b in range(first_b, N - a + 1, K):
    print(b, end=' ')
    ok = True

if not ok:
    print('-1')