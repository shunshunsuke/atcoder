from sys import stdin


def expected(x):
    return (x * (1 + x) / 2) / x


N, K = [int(x) for x in stdin.readline().rstrip().split()]
P = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
prev = 0
for i in range(K):
    ans += expected(P[i])
    prev += expected(P[i])
for i in range(1, N - K + 1):
    tmp = prev - expected(P[i - 1]) + expected(P[i + K - 1])
    prev = tmp
    if tmp > ans:
        ans = tmp
print(ans)
