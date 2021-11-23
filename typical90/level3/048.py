from sys import stdin
import heapq

N, K = [int(x) for x in stdin.readline().rstrip().split()]
targets = []
for i in range(N):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    targets.append(B * -1)
    targets.append((A - B) * -1)
heapq.heapify(targets)
ans = 0
for _ in range(K):
    ans += heapq.heappop(targets) * -1
print(ans)
