from sys import stdin

def get_dists(t):
    stack = [t]
    dists = [-1] * N
    dists[t] = 0
    while len(stack) > 0:
        now = stack.pop()
        for nex in roads[now]:
            if dists[nex] == -1:
                dists[nex] = dists[now] + 1
                stack.append(nex)
    return dists

N = int(stdin.readline().rstrip())
roads = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    a, b = a - 1, b - 1
    roads[a].append(b)
    roads[b].append(a)

# まず頂点1から各頂点までの最短距離を求める
dists = get_dists(0)
# 最も最短距離が大きかった頂点からの最短距離を求める
t = dists.index(max(dists))
dists = get_dists(t)
# その最大値が木の直径
print(max(dists) + 1)
