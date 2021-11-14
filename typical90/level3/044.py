from sys import stdin
from collections import deque

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
A = deque([int(x) for x in stdin.readline().rstrip().split()])

for _ in range(Q):
    T, x, y = [int(x) for x in stdin.readline().rstrip().split()]
    x, y = x - 1, y - 1
    if T == 1:
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        v = A.pop()
        A.appendleft(v)
    else:
        print(A[x])
