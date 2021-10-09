from sys import stdin

N, W = [int(x) for x in stdin.readline().rstrip().split()]
STP = {}
for _ in range(N):
    s, t, p = [int(x) for x in stdin.readline().rstrip().split()]
    STP[s] = STP.get(s, 0) + p
    STP[t] = STP.get(t, 0) - p
STP = sorted(STP.items())
ans = 'Yes'
total = 0
for stp in STP:
    total += stp[1]
    if total > W:
        ans = 'No'
        break
print(ans)
