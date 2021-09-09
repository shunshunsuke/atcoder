from sys import stdin

H, W, N, = [int(x) for x in stdin.readline().rstrip().split()]
hl = set()
wl = set()
nl = []
for _ in range(N):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    hl.add(A - 1)
    wl.add(B - 1)
    nl.append((A - 1, B - 1))
hl = sorted(list(hl))
wl = sorted(list(wl))
hd = {}
for i, h in enumerate(hl):
    hd[h] = i + 1
wd = {}
for i, w in enumerate(wl):
    wd[w] = i + 1
for hw in nl:
    ans = [str(hd[hw[0]]), str(wd[hw[1]])]
    print(' '.join(ans))
