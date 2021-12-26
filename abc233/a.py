from sys import stdin

x, y = [int(x) for x in stdin.readline().rstrip().split()]
a = y - x
if a < 0:
    print(0)
else:
    d, m = divmod(a, 10)
    if m > 0:
        print(d + 1)
    else:
        print(d)
