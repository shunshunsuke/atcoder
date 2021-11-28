from sys import stdin

S = stdin.readline().rstrip()
K = int(stdin.readline().rstrip())
n = len(S)
# 累積和
cnt = [0] * (n + 1)
for i in range(n):
    if S[i] == '.':
        cnt[i + 1] = cnt[i] + 1
    else:
        cnt[i + 1] = cnt[i]

ans = 0
r = 0
for l in range(n):
    while r <= n - 1 and cnt[r + 1] - cnt[l] <= K:
        r += 1
    ans = max(ans, r - l)
print(ans)
