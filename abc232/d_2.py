from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
C = []
for _ in range(H):
    c = stdin.readline().rstrip()
    C.append(list(c))
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        if dp[h][w] <= 0:
            continue
        if h < H - 1 and C[h + 1][w] == '.':
            dp[h + 1][w] = max(dp[h][w] + 1, dp[h + 1][w])
        if w < W - 1 and C[h][w + 1] == '.':
            dp[h][w + 1] = max(dp[h][w] + 1, dp[h][w + 1])
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, dp[h][w])
print(ans)
