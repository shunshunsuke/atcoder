from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]

M = 3001
dp = [[0] * M for _ in range(N)]
for j in range(A[0], B[0] + 1):
    dp[0][j] += 1

for i in range(N):
    for j in range(A[i], B[i] + 1):
        if i > 0:
            dp[i][j] = dp[i - 1][j]
    for j in range(M - 1):
        dp[i][j + 1] += dp[i][j]
        dp[i][j + 1] %= 998244353

print(dp[N - 1][B[N - 1]])
