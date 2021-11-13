from sys import stdin
import itertools

N = int(stdin.readline().rstrip())
times = []
for _ in range(N):
    A = [int(x) for x in stdin.readline().rstrip().split()]
    times.append(A)
M = int(stdin.readline().rstrip())
XY = {}
for _ in range(M):
    x, y = [int(x) for x in stdin.readline().rstrip().split()]
    x, y = x - 1, y - 1
    vx = XY.get(x, [])
    vx.append(y)
    XY[x] = vx
    vy = XY.get(y, [])
    vy.append(x)
    XY[y] = vy

ans = float('inf')
for order in itertools.permutations(list(range(N)), N):
    prev = -1
    tmp = 0
    valid = True
    for i in range(N):
        person = order[i]
        if i > 0:
            v = XY.get(person, [])
            if prev in v:
                valid = False
                break
        prev = person
        tmp += times[person][i]
    if valid:
        ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
