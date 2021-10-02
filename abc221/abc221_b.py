from sys import stdin
import copy

S = list(stdin.readline().rstrip())
T = list(stdin.readline().rstrip())
if S == T:
    print('Yes')
    exit()
for i in range(len(S) - 1):
    ss = copy.copy(S)
    ss[i], ss[i + 1] = ss[i + 1], ss[i]
    if ss == T:
        print('Yes')
        exit()
print('No')
