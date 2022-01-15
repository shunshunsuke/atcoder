from sys import stdin

N, L = [int(x) for x in stdin.readline().rstrip().split()]
K = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
l = 0
r = L
while r - l > 1:
    mid = l + (r - l) // 2
    ok = False
    tmp, num = 0, 0
    for i in range(N):
        if A[i] - tmp >= mid:
            num += 1
            tmp = A[i]
        if num == K:
            if L - A[i] >= mid:
                ok = True
            else:
                break
    if ok:
        l = mid
    else:
        r = mid
print(l)
