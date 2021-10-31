from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
front = [-1] * N
back = [-1] * N
for _ in range(Q):
    q = [int(x) for x in stdin.readline().rstrip().split()]
    if q[0] == 3:
        x = q[1] - 1
        while front[x] != -1:
            x = front[x]
        ans = [x + 1]
        while back[x] != -1:
            x = back[x]
            ans.append(x + 1)
        print(len(ans), *ans)
    else:
        x, y = q[1] - 1, q[2] - 1
        if q[0] == 1:
            back[x] = y
            front[y] = x
        else:
            back[x] = -1
            front[y] = -1
