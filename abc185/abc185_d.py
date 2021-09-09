import math
from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
A.sort()
k = float('inf')
diffs = []
for i in range(len(A) + 1):
    if i == 0:
        prev = 0
    else:
        prev = A[i - 1]
    if i == len(A):
        current = N + 1
    else:
        current = A[i]
    diff = current - prev - 1
    if diff <= 0:
        continue
    diffs.append(diff)
    if diff < k:
        k = diff
ans = 0
for diff in diffs:
    ans += math.ceil(diff / k)
print(ans)
