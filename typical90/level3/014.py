from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]

ans = 0
A.sort()
B.sort()
for i in range(N):
    ans += abs(A[i] - B[i])
print(ans)
