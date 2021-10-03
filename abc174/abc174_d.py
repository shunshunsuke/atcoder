from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
C = list(stdin.readline().rstrip())
R = []
W = deque([])
for i in range(len(C)):
    if C[i] == 'R':
        R.append(i)
    else:
        W.append(i)

ans = 0
while True:
    if len(R) == 0 or len(W) == 0:
        break
    r_max = R.pop()
    w_min = W.popleft()
    if r_max < w_min:
        break
    ans += 1
print(ans)
