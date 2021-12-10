from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
G = [[] for _ in range(N)]
for i in range(M):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(N):
    g = G[i]
    if len(g) >= 2:
        g.sort()
        if g[0] < i < g[1]:
            ans += 1
    elif len(g) == 1:
        if g[0] < i:
            ans += 1
print(ans)
