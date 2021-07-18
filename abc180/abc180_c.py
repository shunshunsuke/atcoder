N = int(input())
if N == 1:
    print(1)
    exit()
ans = [1, N]
n = 2
while n * n <= N:
    res = divmod(N, n)
    if res[1] == 0:
        ans.append(n)
        if res[0] != n:
            ans.append(res[0])
    n += 1
ans.sort()
for a in ans:
    print(a)
