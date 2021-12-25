from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
p = 0
num = {A[0]: 1}
for i in range(N):
    if i > 0:
        num[A[i - 1]] -= 1
        if num[A[i - 1]] <= 0:
            del num[A[i - 1]]
    while True:
        if len(num) <= K:
            p += 1
            if p >= N:
                break
            num[A[p]] = num.get(A[p], 0) + 1
        else:
            break
    ans = max(ans, p - i)
print(ans)
