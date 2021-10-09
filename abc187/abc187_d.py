from sys import stdin

N = int(stdin.readline().rstrip())
AB = []
aoki = 0
taka = 0
for _ in range(N):
    ab = [int(x) for x in stdin.readline().rstrip().split()]
    aoki += ab[0]
    AB.append(ab)
AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)
ans = 0
for ab in AB:
    aoki -= ab[0]
    taka += ab[0] + ab[1]
    ans += 1
    if taka > aoki:
        break
print(ans)
