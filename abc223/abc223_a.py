from sys import stdin

n = int(stdin.readline().rstrip())
q, mod = divmod(n, 100)
if q > 0 and mod == 0:
    print('Yes')
else:
    print('No')
