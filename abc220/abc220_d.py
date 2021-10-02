from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
dp = [[0] * 10 for i in range(N)]
dp[0][A[0]] = 1
for n in range(1, N):
    for i in range(10):
        dp[n][(i + A[n]) % 10] = (dp[n][(i + A[n]) % 10] + dp[n - 1][i]) % 998244353
        dp[n][(i * A[n]) % 10] = (dp[n][(i * A[n]) % 10] + dp[n - 1][i]) % 998244353
for i in range(10):
    print(int(dp[N - 1][i] % 998244353))
