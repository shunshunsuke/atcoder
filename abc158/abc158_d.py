from sys import stdin
from collections import deque

S = stdin.readline().rstrip()
Q = int(stdin.readline().rstrip())
A = deque()
B = []
reverse = False
for _ in range(Q):
    com = list(stdin.readline().rstrip().split())
    if com[0] == '1':
        reverse = not reverse
    else:
        if com[1] == '1':
            if reverse:
                B.append(com[2])
            else:
                A.appendleft(com[2])
        else:
            if reverse:
                A.appendleft(com[2])
            else:
                B.append(com[2])

if reverse:
    A.reverse()
    a = ''.join(list(A))
    b = ''.join(B[::-1])
    s = ''.join(list(S)[::-1])
    print(b + s + a)
else:
    a = ''.join(A)
    b = ''.join(B)
    print(a + S + b)
