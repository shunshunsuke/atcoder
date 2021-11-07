from sys import stdin
import math

t = int(stdin.readline().rstrip())
l, x, y = [int(x) for x in stdin.readline().rstrip().split()]
q = int(stdin.readline().rstrip())
p = math.pi
r = l / 2
for _ in range(q):
    e = int(stdin.readline().rstrip())
    angle = 2 * p * e / t
    # e分の観覧車の位置
    ye = -r * math.sin(angle)
    ze = r - r * math.cos(angle)
    # 観覧車のxy平面座標と像の距離
    tmp = x**2 + (y - ye)**2
    dist = pow(tmp, 0.5)
    # 俯角
    dep = math.atan2(ze, dist)
    print(math.degrees(dep))
