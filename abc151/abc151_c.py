N, M = map(int, input().split())
ac = 0
wa = 0
d = {}
for _ in range(M):
    p, S = input().split()
    p = int(p)
    w = d.get(p, 0)
    if S == 'AC':
        if w == -1:
            continue
        ac += 1
        wa += w
        d[p] = -1
    else:
        if w != -1:
            d[p] = w + 1
print(ac, wa)
