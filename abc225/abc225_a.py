from sys import stdin

a = set(list(stdin.readline().rstrip()))
if len(a) == 3:
    print(6)
elif len(a) == 2:
    print(3)
else:
    print(1)
