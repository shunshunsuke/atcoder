from sys import stdin
from collections import deque

Q = int(stdin.readline().rstrip())
deck = deque([])
for i in range(Q):
    t, x = [int(x) for x in stdin.readline().rstrip().split()]
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x - 1])
