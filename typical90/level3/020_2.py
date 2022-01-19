from sys import stdin

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]

if a < pow(c, b):
    print('Yes')
else:
    print('No')
