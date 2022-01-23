from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip().split()
T = stdin.readline().rstrip().split()
se = set(T)
for s in S:
    if s in se:
        print('Yes')
    else:
        print('No')
