from sys import stdin

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = [int(x) for x in stdin.readline().rstrip().split()]
ans = a // gcd(a, b) * b
if ans > 10**18:
    print('Large')
else:
    print(ans)
