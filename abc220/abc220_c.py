from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
X = int(stdin.readline().rstrip())

div, mod = divmod(X, sum(A))
ans = len(A) * div
s = 0
for i in range(len(A)):
    s += A[i]
    if s > mod:
        ans += i + 1
        break
print(ans)
