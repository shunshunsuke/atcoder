from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
A = []
for i in range(H):
    A.append([int(x) for x in stdin.readline().rstrip().split()])
for i in range(W):
    ans = []
    for j in range(H):
        ans.append(A[j][i])
    print(' '.join([str(x) for x in ans]))
