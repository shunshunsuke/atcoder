from sys import stdin
import array
import bisect

L, Q = [int(x) for x in stdin.readline().rstrip().split()]
separation = array.array('i', [0, L])
for _ in range(Q):
    c, x = [int(x) for x in stdin.readline().rstrip().split()]
    if c == 1:
        bisect.insort(separation, x)
    else:
        i = bisect.bisect(separation, x)
        print(separation[i] - separation[i - 1])
