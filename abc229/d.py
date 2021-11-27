from sys import stdin

S = stdin.readline().rstrip()
K = int(stdin.readline().rstrip())
l = 0
r = len(S)
while l <= r:
    c = (l + r) // 2
    ok = False
    num = 0
    for i in range(len(S) - c + 1):
        if i == 0:
            num = S.count('.', 0, c)
        else:
            if S[i - 1] == '.':
                num -= 1
            if S[i + c - 1] == '.':
                num += 1
        if num <= K:
            ok = True
            break
    if ok:
        l = c + 1
    else:
        r = c - 1
print(l - 1)
