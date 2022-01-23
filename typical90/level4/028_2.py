from sys import stdin

N = int(stdin.readline().rstrip())
tiles = [[0] * 1001 for _ in range(1001)]
# 重みの加算
for i in range(N):
    lx, ly, rx, ry = [int(x) for x in stdin.readline().rstrip().split()]
    tiles[ly][lx] += 1
    tiles[ry][lx] -= 1
    tiles[ly][rx] -= 1
    tiles[ry][rx] += 1
# 横方向への累積和
for y in range(1001):
    for x in range(1, 1001):
        tiles[y][x] += tiles[y][x - 1]
# 縦方向への累積和
for y in range(1, 1001):
    for x in range(1001):
        tiles[y][x] += tiles[y - 1][x]
ans = [0] * N
for rows in tiles:
    for dot in rows:
        if dot > 0:
            ans[dot - 1] += 1
for a in ans:
    print(a)
