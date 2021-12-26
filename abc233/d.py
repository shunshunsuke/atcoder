import collections
from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
total = [0] * (N + 1)
for i in range(N):
    total[i + 1] = total[i] + A[i]
ans = 0
c = collections.Counter(total)
for i in range(1, N + 1):
    c[total[i - 1]] -= 1
    ans += c[total[i - 1] + K]
print(ans)
