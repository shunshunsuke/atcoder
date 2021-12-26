from sys import stdin

L, R = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()
ans = ''
if L - 1 > 0:
    ans += S[:L - 1]
ans += S[L - 1:R][::-1]
if R < len(S):
    ans += S[R:]
print(ans)
