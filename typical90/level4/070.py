import statistics
from sys import stdin

N = int(stdin.readline().rstrip())
X, Y = [], []
for _ in range(N):
    x, y = [int(x) for x in stdin.readline().rstrip().split()]
    X.append(x)
    Y.append(y)
ax = statistics.median(X)
ay = statistics.median(Y)
ans = 0
for x in X:
    ans += abs(x - ax)
for y in Y:
    ans += abs(y - ay)
print(int(ans))
