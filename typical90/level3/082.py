from sys import stdin

mod = 10**9 + 7
L, R = [int(x) for x in stdin.readline().rstrip().split()]
ll = len(str(L))
rl = len(str(R))
ans = 0
for i in range(ll, rl + 1):
    s = 10**(i - 1)
    e = int('9' * i)
    if i == ll:
        s = L
    if i == rl:
        e = R
    tmp = (e - s + 1) * (s + e) // 2
    ans += i * tmp
print(ans % mod)
