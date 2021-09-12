from sys import stdin

n = int(stdin.readline().rstrip())
s = list(stdin.readline().rstrip())
if s[n - 1] == 'o':
    print('Yes')
else:
    print('No')
