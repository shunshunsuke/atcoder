from sys import stdin

n = stdin.readline().rstrip()
if len(n) == 1:
    n = '000' + n
elif len(n) == 2:
    n = '00' + n
elif len(n) == 3:
    n = '0' + n
print(n)
