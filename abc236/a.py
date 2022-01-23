from sys import stdin

S = list(stdin.readline().rstrip())
a, b = [int(x) for x in stdin.readline().rstrip().split()]
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print(''.join(S))
