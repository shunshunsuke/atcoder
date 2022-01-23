import collections
from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
start = 0
end = 0
dic = {A[0]: 1}
ans = 0
while True:
    if len(dic) > K:
        dic[A[start]] -= 1
        if dic[A[start]] == 0:
            del dic[A[start]]
        ans = max(ans, end - start)
        start += 1
    else:
        end += 1
        if end >= N:
            ans = max(ans, end - start)
            break
        dic[A[end]] = dic.get(A[end], 0) + 1
print(ans)
