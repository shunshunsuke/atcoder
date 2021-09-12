import itertools
from sys import stdin

N = int(stdin.readline().rstrip())
XY = []
XY_dict = {}
for _ in range(N):
    xyl = list(map(int, stdin.readline().rstrip().split()))
    XY.append(xyl)
    XY_dict[str(xyl)] = True

XY.sort()
ans = 0
for xy in itertools.combinations(XY, 2):
    # 左下の点とする
    lb = xy[0]
    # 右上の点とする
    rt = xy[1]
    if lb[0] >= rt[0] or lb[1] >= rt[1]:
        continue
    if not XY_dict.get(str([lb[0], rt[1]]), False):  # 左上の点が存在するか
        continue
    if not XY_dict.get(str([rt[0], lb[1]]), False):  # 右下の点が存在するか
        continue
    ans += 1
print(ans)
