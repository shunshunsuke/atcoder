from sys import stdin

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
min_gcd = min(gcd(a, b), gcd(b, c), gcd(a, c))
ans = (a // min_gcd - 1) + (b // min_gcd - 1) + (c // min_gcd - 1)
print(ans)
