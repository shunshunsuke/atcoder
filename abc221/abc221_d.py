from sys import stdin

N = int(stdin.readline().rstrip())
x = []
for _ in range(N):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    x.append([a, 1])
    x.append([a + b, -1])
x.sort()
ans = {}
cnt = 0
for i in range(len(x) - 1):
    cnt += x[i][1]
    ans[cnt] = ans.get(cnt, 0) + ((x[i + 1][0]) - (x[i][0]))

for i in range(1, N + 1):
    if i == N:
        print(ans.get(i, 0), end="")
    else:
        print(ans.get(i, 0), end=" ")
