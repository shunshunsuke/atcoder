import itertools

N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
ans = float('inf')
l = list(range(N))
for num in range(1, N + 1):
    for cc in itertools.combinations(l, num):
        money = 0
        skills = [0] * M
        for c in cc:
            for j in range(M + 1):
                if j == 0:
                    money += A[c][0]
                else:
                    skills[j - 1] += A[c][j]
        if all([skill >= X for skill in skills]):
            ans = min(ans, money)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
