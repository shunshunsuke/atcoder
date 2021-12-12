from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
now = 0
ans = 0
while True:
    if now >= N:
        break
    ns = S[now]
    tgt = 'o'
    if ns == 'o':
        tgt = 'x'
    nex = now + 1
    while True:
        if nex >= N:
            break
        if S[nex] == tgt:
            ans += (nex - now) * (N - nex)
            break
        nex += 1
    now = nex
print(ans)
