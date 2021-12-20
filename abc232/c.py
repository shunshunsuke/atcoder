import itertools
from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
taka = []
for _ in range(M):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    taka.append([a, b])
aoki = set()
for _ in range(M):
    c, d = [int(x) for x in stdin.readline().rstrip().split()]
    aoki.add(str(c) + str(d))

P = []
for i in range(N):
    P.append(i + 1)
for v in itertools.permutations(P, N):
    ok = True
    for ab in taka:
        a, b = ab[0], ab[1]
        c = v[a - 1]
        d = v[b - 1]
        if c > d:
            c, d = d, c
        if str(c) + str(d) not in aoki:
            ok = False
            break
    if ok:
        print('Yes')
        exit()
print('No')
