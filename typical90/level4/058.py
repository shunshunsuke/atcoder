from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
mod = 10**5
vis = [-1] * mod
vis[N] = 0
by = 0
while True:
    by += 1
    N = (N + sum(map(int, list(str(N))))) % mod
    if by == K:
        print(N)
        exit()
    if vis[N] > -1:
        break
    vis[N] = by
cycle = by - vis[N]
ind = (K - by) % cycle
for _ in range(ind):
    N = (N + sum(map(int, list(str(N))))) % mod
print(N)
