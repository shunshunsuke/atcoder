from sys import stdin

N, P = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
for a in A:
    if a < P:
        ans += 1
print(ans)
