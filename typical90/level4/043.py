from sys import stdin
from collections import deque

H, W = [int(x) for x in stdin.readline().rstrip().split()]
rs, cs = [int(x) for x in stdin.readline().rstrip().split()]
rs, cs = rs - 1, cs - 1
rt, ct = [int(x) for x in stdin.readline().rstrip().split()]
rt, ct = rt - 1, ct - 1
B = []
for _ in range(H):
    S = list(stdin.readline().rstrip())
    B.append(S)
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def inside(i, j):
    return 0 <= i < H and 0 <= j < W


deq = deque()
deq.append([rs, cs, -1, -1])
ans = [[float('inf')] * W for _ in range(H)]
ans[rs][cs] = 0
while len(deq) > 0:
    i, j, d, cnt = deq.popleft()
    for ind in range(4):
        nex_i = i + di[ind]
        nex_j = j + dj[ind]
        if not inside(nex_i, nex_j): continue
        if B[nex_i][nex_j] == '#': continue
        nex_cnt = cnt + (d != ind)
        if ans[nex_i][nex_j] >= nex_cnt:
            ans[nex_i][nex_j] = nex_cnt
            if cnt == nex_cnt:
                deq.appendleft([nex_i, nex_j, ind, nex_cnt])
            else:
                deq.append([nex_i, nex_j, ind, nex_cnt])

print(ans[rt][ct])
