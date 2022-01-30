from sys import stdin

S = stdin.readline().rstrip()
if S == S[::-1]:
    print('Yes')
    exit()
N = len(S)
num_back = 0
for i in range(N - 1, -1, -1):
    if S[i] == 'a':
        num_back += 1
    else:
        break
num_front = 0
for i in range(N):
    if S[i] == 'a':
        num_front += 1
    else:
        break
tgt = num_back - num_front
if tgt > 0:
    new_s = 'a' * tgt + S
    if new_s == new_s[::-1]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
