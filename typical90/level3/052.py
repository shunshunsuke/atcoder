from sys import stdin

N = int(stdin.readline().rstrip())
ans = 1
for i in range(N):
    A = [int(x) for x in stdin.readline().rstrip().split()]
    ans *= sum(A)
    ans %= 10**9 + 7
print(ans)
