import itertools
from sys import stdin

N, X = [int(x) for x in stdin.readline().rstrip().split()]
A = []
for _ in range(N):
    LA = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(LA[1:])
ans = 0
for aa in list(itertools.product(*A)):
    tmp = 1
    for a in aa:
        tmp *= a
        if tmp > X:
            break
    if tmp == X:
        ans += 1
print(ans)
