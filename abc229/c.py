from sys import stdin

N, W = [int(x) for x in stdin.readline().rstrip().split()]
AB = []
ans = 0
g = 0
for i in range(N):
    ab = [int(x) for x in stdin.readline().rstrip().split()]
    AB.append(ab)
AB.sort(reverse=True)
for ab in AB:
    a, b = ab[0], ab[1]
    if g + b <= W:
        ans += a * b
        g += b
    else:
        ans += a * (W - g)
        break
print(ans)
