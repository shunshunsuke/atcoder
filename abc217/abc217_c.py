from sys import stdin

N = int(stdin.readline().rstrip())
p = [int(x) for x in stdin.readline().rstrip().split()]
ans = [0] * N
for i in range(N):
    ans[p[i] - 1] = str(i + 1)
print(' '.join(ans))
