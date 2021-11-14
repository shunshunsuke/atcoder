from sys import stdin
import math

H, W = [int(x) for x in stdin.readline().rstrip().split()]
if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    ans = math.ceil(H / 2) * math.ceil(W / 2)
    print(ans)
