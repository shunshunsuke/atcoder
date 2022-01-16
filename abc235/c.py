from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
dic = {}
for i in range(N):
    arr = dic.get(A[i], [])
    arr.append(i)
    dic[A[i]] = arr
for i in range(Q):
    x, k = [int(x) for x in stdin.readline().rstrip().split()]
    arr = dic.get(x, -1)
    if arr == -1 or k - 1 >= len(arr):
        print(-1)
    else:
        print(arr[k - 1] + 1)
