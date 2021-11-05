from sys import stdin
import bisect

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
A.sort()
Q = int(stdin.readline().rstrip())
for _ in range(Q):
    b = int(stdin.readline().rstrip())
    ind = bisect.bisect_left(A, b)
    if ind == 0:
        print(abs(A[ind] - b))
    elif ind == len(A):
        print(abs(A[-1] - b))
    else:
        left = abs(A[ind - 1] - b)
        right = abs(A[ind] - b)
        print((min(left, right)))
