from sys import stdin

N = int(stdin.readline().rstrip())
T = []
A = []
for _ in range(N):
    TKA = [int(x) for x in stdin.readline().rstrip().split()]
    t, k = TKA[0], TKA[1]
    T.append(t)
    a = []
    if k > 0:
        a = list(map(lambda x: x - 1, TKA[2:]))
    A.append(a)

need = [False] * N
need[N - 1] = True
for i in reversed(range(0, N)):
    if need[i]:
        for a in A[i]:
            need[a] = True

ans = 0
for i in range(N):
    if need[i]:
        ans += T[i]
print(ans)
