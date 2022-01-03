from sys import stdin
import itertools

H, W = [int(x) for x in stdin.readline().rstrip().split()]
PS = []
for _ in range(H):
    P = [int(x) for x in stdin.readline().rstrip().split()]
    PS.append(P)

ans = 0
for bit in itertools.product((0, 1), repeat=H):
    if bit.count(1) == 0:
        continue
    tmp = []
    for i in range(H):
        if bit[i]:
            tmp.append(PS[i])
    w_max = 0
    nums = {}
    for w in range(W):
        tgt = tmp[0][w]
        ok = True
        for h in range(1, len(tmp)):
            if tmp[h][w] != tgt:
                ok = False
                break
        if ok:
            nums[tgt] = nums.get(tgt, 0) + 1
            w_max = max(w_max, nums[tgt])
    ans = max(ans, len(tmp) * w_max)

print(ans)
