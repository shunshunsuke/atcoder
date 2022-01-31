from sys import stdin
from collections import deque

H, W = [int(x) for x in stdin.readline().rstrip().split()]
sx, sy = [int(x) for x in stdin.readline().rstrip().split()]
gx, gy = [int(x) for x in stdin.readline().rstrip().split()]
sx, sy, gx, gy = sx - 1, sy - 1, gx - 1, gy - 1
S = []
for i in range(H):
    S.append(list(stdin.readline().rstrip()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[[float('inf') for _ in range(4)] for _ in range(1009)] for _ in range(1009)]
deq = deque([])
for i in range(4):
    dist[sx][sy][i] = 0
    deq.append([sx, sy, i])
while len(deq) > 0:
    u = deq.popleft()
    for i in range(4):
        tx = u[0] + dx[i]
        ty = u[1] + dy[i]
        cost = dist[u[0]][u[1]][u[2]] + (1 if u[2] != i else 0)
        if 0 <= tx < H and 0 <= ty < W and S[tx][ty] == '.' and dist[tx][ty][i] > cost:
            dist[tx][ty][i] = cost
            if u[2] != i:
                # 方向が異なりコスト=1なので最後尾に追加
                deq.append([tx, ty, i])
            else:
                # 方向が同じでコスト=0なので先頭に追加
                deq.appendleft([tx, ty, i])

ans = float('inf')
for i in range(4):
    ans = min(ans, dist[gx][gy][i])
print(ans)
