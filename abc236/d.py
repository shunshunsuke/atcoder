import copy
import itertools
from sys import stdin

def dfs(s, x):
    # まず残っている中から最小のものを選ぶ
    si = -1
    for i in range(2 * N):
        if not s[i]:
            si = i
            break
    # すべて選んだので終わり
    if si == -1:
        global ans
        ans = max(ans, x)
        return
    # siの相方を探す
    s[si] = True
    for i in range(2 * N):
        if not s[i]:
            s_copy = copy.copy(s)
            s_copy[i] = True
            dfs(s_copy, x ^ A[si][i - si - 1])


N = int(stdin.readline().rstrip())
A = []
for _ in range(2 * N - 1):
    a = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(a)
ans = 0
dfs([False] * 2 * N, 0)
print(ans)
