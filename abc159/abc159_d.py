from sys import stdin
import collections
import math


def permutations_count(n, r):
    if n <= 1:
        return 0
    else:
        if n in ans:
            return ans[n]
        else:
            ans[n] = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
            return ans[n]


N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
a_count = collections.Counter(A)
ans = {}
s = 0
for k in a_count.keys():
    s += permutations_count(a_count[k], 2)
for i in range(N):
    print(s - (permutations_count(a_count[A[i]], 2) - permutations_count(a_count[A[i]] - 1, 2)))
