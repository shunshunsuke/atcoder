import collections
from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) % 46 for x in stdin.readline().rstrip().split()]
B = [int(x) % 46 for x in stdin.readline().rstrip().split()]
C = [int(x) % 46 for x in stdin.readline().rstrip().split()]
a_cnt = collections.Counter(A)
b_cnt = collections.Counter(B)
c_cnt = collections.Counter(C)
ans = 0
for x in range(46):
    for y in range(46):
        for z in range(46):
            if (x + y + z) % 46 == 0:
                ans += a_cnt[x] * b_cnt[y] * c_cnt[z]
print(ans)
