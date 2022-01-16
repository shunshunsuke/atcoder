import copy
from sys import stdin

a, N = [int(x) for x in stdin.readline().rstrip().split()]
dup = set()
num = 0
now = []
nxt = [N]
ok = False
while len(nxt) > 0:
    if 1 in nxt:
        ok = True
        break
    now = copy.copy(nxt)
    nxt = []
    for n in now:
        if n in dup:
            continue
        # 割る
        if n % a == 0:
            nxt.append(n // a)
        # 入れ替える
        n_str = str(n)
        if n >= 10 and n_str[1] != '0':
            nxt.append(int(n_str[1:] + n_str[0]))
        dup.add(n)
    num += 1
if ok:
    print(num)
else:
    print(-1)
