import collections
from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    a, b = a - 1, b - 1
    sides[a].append(b)
    sides[b].append(a)

G = [None] * N
G[0] = True
queue = deque([0])
while len(queue) > 0:
    tgt = queue.popleft()
    for nxt in sides[tgt]:
        if G[nxt] is None:
            G[nxt] = not G[tgt]
            queue.append(nxt)
cnt = collections.Counter(G)
x = True
if cnt[False] > cnt[True]:
    x = False
ans = []
for i in range(N):
    if G[i] == x and len(ans) < N // 2:
        ans.append(str(i + 1))
print(' '.join(ans))

