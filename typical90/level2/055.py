from sys import stdin

n, p, q = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) % p for x in stdin.readline().rstrip().split()]
ans = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if A[i] * A[j] % p * A[k] % p * A[l] % p * A[m] % p == q:
                        ans += 1
print(ans)
