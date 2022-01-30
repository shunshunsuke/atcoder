from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
ans = deque([N])
for i in range(N - 1, -1, -1):
    if S[i] == 'R':
        ans.appendleft(i)
    else:
        ans.append(i)
print(' '.join([str(x) for x in ans]))
