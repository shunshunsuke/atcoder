import itertools
from sys import stdin

S, K = stdin.readline().rstrip().split()
S = list(S)
K = int(K)
ans = list(set(itertools.permutations(S, len(S))))
ans.sort()
print(''.join(ans[K - 1]))
