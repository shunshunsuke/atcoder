from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()
alpha2num = lambda c: ord(c) - ord('A') + 1
diff = alpha2num(T[0]) - alpha2num(S[0])
if diff < 0:
    diff += 26
ok = True
for i in range(len(S)):
    d = alpha2num(T[i]) - alpha2num(S[i])
    if d < 0:
        d += 26
    if d != diff:
        ok = False
        break
if ok:
    print('Yes')
else:
    print('No')
