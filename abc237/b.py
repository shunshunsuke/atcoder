from sys import stdin
import numpy as np

H, W = [int(x) for x in stdin.readline().rstrip().split()]
A = []
for i in range(H):
    a = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(a)
ans = np.array(A).T
for a in ans:
    print(' '.join([str(x) for x in a]))
