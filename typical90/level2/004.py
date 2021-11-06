from operator import add
from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
board = []
sum_h = []
sum_w = [0] * W
for _ in range(H):
    A = [int(x) for x in stdin.readline().rstrip().split()]
    board.append(A)
    sum_h.append(sum(A))
    sum_w = list(map(add, sum_w, A))

ans = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        ans[h][w] = sum_h[h] + sum_w[w] - board[h][w]

for a in ans:
    a = map(str, a)
    print(' '.join(a))
