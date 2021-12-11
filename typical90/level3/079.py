from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
A = []
for i in range(H):
    aa = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(aa)
B = []
for i in range(H):
    bb = [int(x) for x in stdin.readline().rstrip().split()]
    B.append(bb)

ans = 0
for h in range(H - 1):
    for w in range(W - 1):
        t = B[h][w] - A[h][w]
        if t == 0:
            continue
        ans += abs(t)
        A[h][w] += t
        A[h + 1][w] += t
        A[h][w + 1] += t
        A[h + 1][w + 1] += t

if A == B:
    print('Yes')
    print(ans)
else:
    print('No')
