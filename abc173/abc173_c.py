import itertools
from sys import stdin

h, w, k = [int(x) for x in stdin.readline().rstrip().split()]
grid = []
for _ in range(h):
    c = list(stdin.readline().rstrip())
    grid.append(c)

ans = 0
TF = [True, False]
for htf in itertools.product(TF, repeat=h):
    for wtf in itertools.product(TF, repeat=w):
        total = 0
        for hi in range(h):
            if htf[hi]:
                continue
            for wi in range(w):
                if wtf[wi]:
                    continue
                if grid[hi][wi] == '#':
                    total += 1
        if total == k:
            ans += 1

print(ans)
