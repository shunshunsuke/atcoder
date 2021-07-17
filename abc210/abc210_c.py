from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
C = list(map(int, stdin.readline().rstrip().split()))
colors = {}
for c in C[0:K]:
    colors[c] = colors.get(c, 0) + 1
ans = len(colors)
for i in range(1, N - K + 1):
    colors[C[i - 1]] -= 1
    if colors[C[i - 1]] == 0:
        del colors[C[i - 1]]
    colors[C[i + K - 1]] = colors.get(C[i + K - 1], 0) + 1
    ans = max(ans, len(colors))
print(ans)
