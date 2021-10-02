import itertools
from sys import stdin

N = [int(i) for i in list(stdin.readline().rstrip())]
ans = 0
TF = [True, False]
for tf in itertools.product(TF, repeat=len(N)):
    if len(set(tf)) == 1:
        continue
    A = []
    B = []
    for i in range(len(tf)):
        if tf[i]:
            A.append(N[i])
        else:
            B.append(N[i])
    A.sort(reverse=True)
    if A[0] == 0:
        continue
    B.sort(reverse=True)
    if B[0] == 0:
        continue
    cal = int(''.join(map(str, A))) * int(''.join(map(str, B)))
    if cal > ans:
        ans = cal

print(ans)
