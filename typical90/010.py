from sys import stdin

N = int(stdin.readline().rstrip())
A = [0] * (N + 1)
B = [0] * (N + 1)
for i in range(N):
    c, p = [int(x) for x in stdin.readline().rstrip().split()]
    A[i + 1] = A[i]
    B[i + 1] = B[i]
    if c == 1:
        A[i + 1] += p
    else:
        B[i + 1] += p

Q = int(stdin.readline().rstrip())
for _ in range(Q):
    l, r = [int(x) for x in stdin.readline().rstrip().split()]
    print(A[r] - A[l - 1], B[r] - B[l - 1])
