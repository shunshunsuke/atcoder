from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
num = 0
for i in range(N):
    num += abs(A[i] - B[i])

if num > K:
    print('No')
else:
    if (K - num) % 2 == 0:
        print('Yes')
    else:
        print('No')
