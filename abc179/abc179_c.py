import math

N = int(input())
ans = 0
for a in range(1, N):
    ans += math.floor((N - 1) / a)
print(ans)
