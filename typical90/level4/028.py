from sys import stdin
import array

N = int(stdin.readline().rstrip())
tiles = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(N):
    lx, ly, rx, ry = [int(x) for x in stdin.readline().rstrip().split()]
    # 重みの加算
    tiles[ly][lx] += 1
    tiles[ry][lx] -= 1
    tiles[ly][rx] -= 1
    tiles[ry][rx] += 1

# 横方向への累積和
for y in range(1001):
    for x in range(1, 1001):
        tiles[y][x] += tiles[y][x - 1]
# 縦方向の累積和
for y in range(1, 1001):
    for x in range(1001):
        tiles[y][x] += tiles[y - 1][x]

ans = [0] * N
for y in range(1001):
    for x in range(1001):
        t = tiles[y][x]
        if t > 0:
            ans[t - 1] += 1
for a in ans:
    print(a)
