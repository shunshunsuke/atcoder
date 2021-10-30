from sys import stdin

N = int(stdin.readline().rstrip())
AB = []
total_time = 0
for _ in range(N):
    a, b = [int(x) for x in stdin.readline().rstrip().split()]
    total_time += a / b
    AB.append((a, b))
run_time = total_time / 2
ans = 0
for ab in AB:
    a = ab[0]
    b = ab[1]
    if run_time - (a / b) >= 0:
        ans += a
        run_time -= a / b
    else:
        ans += b * run_time
        break
print(ans)
