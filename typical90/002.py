from sys import stdin
import itertools

n = int(stdin.readline().rstrip())
if n % 2 != 0:
    exit()

for A in itertools.product(('(', ')'), repeat=n):
    if A.count('(') != n // 2:
        continue
    l, r = 0, 0
    valid = True
    for a in A:
        if a == '(':
            l += 1
        else:
            r += 1
        if r > l:
            valid = False
    if valid:
        print(''.join(A))

