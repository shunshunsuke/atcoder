from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [0] * (N)
ans = 0
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]
    ans += abs(B[i])
for i in range(Q):
    l, r, v = [int(x) for x in stdin.readline().rstrip().split()]
    l, r = l - 1, r - 1
    mae = abs(B[l - 1]) + abs(B[r])
    if l >= 1:
        B[l - 1] += v
    if r <= N - 2:
        B[r] -= v
    ato = abs(B[l - 1]) + abs(B[r])
    ans += ato - mae
    print(ans)
