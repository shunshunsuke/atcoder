H, W, X, Y = map(int, input().split())
S = [input() for i in range(H)]
ans = 1
xm = X - 2
while xm >= 0:
    if S[xm][Y - 1] == '#':
        break
    ans += 1
    xm -= 1
xp = X
while xp <= H - 1:
    if S[xp][Y - 1] == '#':
        break
    ans += 1
    xp += 1
ym = Y - 2
while ym >= 0:
    if S[X - 1][ym] == '#':
        break
    ans += 1
    ym -= 1
yp = Y
while yp <= W - 1:
    if S[X - 1][yp] == '#':
        break
    ans += 1
    yp += 1
print(ans)
