from sys import stdin

def binpower(x, n):
    ans = 1
    while n:
        if n % 2 == 1:
            ans = ans * x % mod
        x = x * x % mod
        n //= 2
    return ans

N, K = [int(x) for x in stdin.readline().rstrip().split()]
mod = 10**9 + 7
if K == 1:
    print(1 if N == 1 else 0)
elif N == 1:
    print(K % mod)
elif N == 2:
    print((K * (K - 1) % mod))
else:
    ans = (K * (K - 1) % mod) * binpower(K - 2, N - 2) % mod
    print(ans)
