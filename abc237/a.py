from sys import stdin

N = int(stdin.readline().rstrip())
t = 2**31
if -t <= N < t:
    print('Yes')
else:
    print('No')
