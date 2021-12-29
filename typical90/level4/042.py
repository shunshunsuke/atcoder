from sys import stdin

K = int(stdin.readline().rstrip())
if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 1)
dp[0] = 1
for i in range(1, K + 1):
    B = min(i, 9)
    for j in range(1, B + 1):
        dp[i] += dp[i - j] % (10**9 + 7)
print(dp[K] % (10**9 + 7))
