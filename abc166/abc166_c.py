N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    AB[A - 1].append(B - 1)
    AB[B - 1].append(A - 1)

ans = 0
for i in range(N):
    indexes = AB[i]
    targets = []
    for j in indexes:
        targets.append(H[j])
    if len(targets) == 0 or H[i] > max(targets):
        ans += 1
print(ans)
