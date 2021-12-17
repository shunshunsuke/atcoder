from sys import stdin

N, L = [int(x) for x in stdin.readline().rstrip().split()]
K = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
l = 0
r = L
while r - l > 1:
    mid = (l + r) // 2
    tmp = 0
    num = 0
    for i in range(N):
        if A[i] - tmp >= mid and L - A[i] >= mid:
            tmp = A[i]
            num += 1
    if num >= K:
        l = mid
    else:
        r = mid
print(l)
