from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]
x, y = A, B
while y > 0:
    x, y = y, x % y
ans = A * B // x
if ans > 10**18:
    print('Large')
else:
    print(ans)
