from sys import stdin
import copy


def judge(b, e):
    for n in range(b, e, 8):
        tmp_sh = copy.copy(sh)
        is_ok = True
        nl = [int(x) for x in list(str(n))]
        for nn in nl:
            val = tmp_sh.get(nn, 0)
            if val:
                tmp_sh[nn] -= 1
            else:
                is_ok = False
                break
        if is_ok:
            print('Yes')
            exit()


S = list(stdin.readline().rstrip())
sh = {}
for s in S:
    s = int(s)
    sh[s] = sh.get(s, 0) + 1

if len(S) == 1 and S[0] == '8':
    print('Yes')
    exit()
elif len(S) == 2:
    judge(16, 100)
else:
    judge(112, 1000)

print('No')
