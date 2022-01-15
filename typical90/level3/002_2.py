import itertools
from sys import stdin

N = int(stdin.readline().rstrip())
for B in itertools.product(('(', ')'), repeat=N):
    num_0, num_1 = 0, 0
    if B.count('(') != B.count(')'):
        continue
    ok = True
    for b in B:
        if b == '(':
            num_0 += 1
        else:
            num_1 += 1
        if num_1 > num_0:
            ok = False
    if ok:
        print(''.join(B))
