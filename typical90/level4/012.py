from sys import stdin


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


H, W = [int(x) for x in stdin.readline().rstrip().split()]
uf = UnionFind(H * W)
used = [False] * (H * W)
Q = int(stdin.readline().rstrip())
for _ in range(Q):
    q = [int(x) for x in stdin.readline().rstrip().split()]
    if q[0] == 1:
        r, c = q[1] - 1, q[2] - 1
        i = r * W + c
        used[i] = True
        bes = (r - 1) * W + c
        if r > 0 and used[bes]:
            uf.union(i, bes)
        bes = (r + 1) * W + c
        if r < H - 1 and used[bes]:
            uf.union(i, bes)
        bes = r * W + c - 1
        if c > 0 and used[bes]:
            uf.union(i, bes)
        bes = r * W + c + 1
        if c < W - 1 and used[bes]:
            uf.union(i, bes)
    else:
        ra, ca, rb, cb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        ai = ra * W + ca
        bi = rb * W + cb
        if not used[ai] or not used[bi]:
            print('No')
        else:
            if uf.same(ai, bi):
                print('Yes')
            else:
                print('No')
