from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dist = [None] * N
q = deque()
q.append(0)
dist[0] = 0
vs = []
while len(q) > 0:
    v = q.popleft()
    vs.append(v)
    for u in G[v]:
        if dist[u] is not None:
            continue
        dist[u] = dist[v] + 1
        q.append(u)

dp = [0] * N
dp[0] = 1
for v in vs:
    for u in G[v]:
        if dist[u] == dist[v] + 1:
            dp[u] += dp[v]
print(dp[N - 1] % (10**9 + 7))
