from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
if a[0] == '.' and a[1] == '#' and b[0] == '#' and b[1] == '.':
    print('No')
elif a[0] == '#' and a[1] == '.' and b[0] == '.' and b[1] == '#':
    print('No')
else:
    print('Yes')
