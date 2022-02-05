from sys import stdin

def pow(x, n):
    ans = 1
    while n > 0:
        if n % 2:
            ans = ans * x % mod
        x = x * x % mod
        n //= 2
    return ans

N, K = [int(x) for x in stdin.readline().rstrip().split()]
mod = 10**9 + 7
if N == 1:
    print(K)
elif N == 2:
    print(K * (K - 1) % mod)
else:
    if K <= 2:
        print(0)
    else:
        print(K * (K - 1) % mod * pow(K - 2, N - 2) % mod)
