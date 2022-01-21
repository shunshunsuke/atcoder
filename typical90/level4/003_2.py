from sys import stdin

def get_seen(start):
    stack = []
    seen = [-1] * N
    stack.append(start)
    seen[start] = 0
    while len(stack) > 0:
        t = stack.pop()
        for n in G[t]:
            if seen[n] == -1:
                seen[n] = seen[t] + 1
                stack.append(n)
    return seen

N = int(stdin.readline().rstrip())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

edge_seen = get_seen(0)
edge = edge_seen.index(max(edge_seen))
print(max(get_seen(edge)) + 1)
