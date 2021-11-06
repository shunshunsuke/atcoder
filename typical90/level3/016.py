from sys import stdin

n = int(stdin.readline().rstrip())
abc = [int(x) for x in stdin.readline().rstrip().split()]
abc.sort(reverse=True)
a, b, c = abc
ans = 10001
for x in range(n // a + 1):
    m = n - a*x
    for y in range(m // b + 1):
        l = m - b*y
        z, mod = divmod(l, c)
        if mod == 0:
            ans = min(ans, x + y + z)
print(ans)
