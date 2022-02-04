from sys import stdin

N = int(stdin.readline().rstrip())
ans = 1
mod = 10**9 + 7
for _ in range(N):
    A = [int(x) for x in stdin.readline().rstrip().split()]
    ans *= sum(A) % mod
print(ans % mod)
