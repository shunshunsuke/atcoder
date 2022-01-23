import copy
import itertools
from sys import stdin

def hoge(lis, comb, ret):
    for v in itertools.combinations(lis, 2):
        lis_dup = copy.copy(lis)
        comb_dup = copy.copy(comb)
        comb_dup.append(v)
        hoge([i for i in lis_dup if i not in v], comb_dup, ret)
    if len(lis) == 0:
        ret.append(comb)

N = int(stdin.readline().rstrip())
A = []
for _ in range(2*N - 1):
    a = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(a)
lis = [i + 1 for i in range(2*N)]
ret = []
hoge(lis, [], ret)
ans = 0
for rs in ret:
    tmp = 0
    for r in rs:
        tmp ^= A[r[0] - 1][r[1] - r[0] - 1]
    ans = max(ans, tmp)
print(ans)
