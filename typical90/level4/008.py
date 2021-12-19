from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
dp = [[0] * 7 for _ in range(N)]
if S[0] == 'a':
    dp[0][0] = 1
for n in range(1, N):
    for i in range(7):
        dp[n][i] = dp[n - 1][i]

    char = S[n]
    if char == 'a':
        dp[n][0] = dp[n - 1][0] + 1
    elif char == 't':
        dp[n][1] += dp[n - 1][0]
    elif char == 'c':
        dp[n][2] += dp[n - 1][1]
    elif char == 'o':
        dp[n][3] += dp[n - 1][2]
    elif char == 'd':
        dp[n][4] += dp[n - 1][3]
    elif char == 'e':
        dp[n][5] += dp[n - 1][4]
    elif char == 'r':
        dp[n][6] += dp[n - 1][5]

print(dp[N - 1][6] % (10**9 + 7))
