from sys import stdin
import bisect

L, Q = [int(x) for x in stdin.readline().rstrip().split()]
separation = []
for _ in range(Q):
    c, x = [int(x) for x in stdin.readline().rstrip().split()]
    if c == 1:
        bisect.insort(separation, x)
    else:
        i = bisect.bisect(separation, x)
        if len(separation) == 0:
            print(L)
        elif i == 0:
            print(separation[0])
        elif i == len(separation):
            print(L - separation[-1])
        else:
            print(separation[i] - separation[i - 1])
