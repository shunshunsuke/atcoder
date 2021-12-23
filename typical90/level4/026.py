import collections
from sys import stdin

def dfs(pos, cur):
    col[pos] = cur
    for i in G[pos]:
        if col[i] == -1:
            dfs(i, 1 - cur)

N = int(stdin.readline().rstrip())
G = [[] for _ in range(N)]
col = [-1] * N
for _ in range(N - 1):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)
dfs(0, 0)
cou = collections.Counter(col)
t = 0 if cou[0] >= cou[1] else 1
num = 0
ans = []
for i in range(N):
    if len(ans) >= N / 2:
        break
    if col[i] == t:
        ans.append(i + 1)
print(*ans)
    