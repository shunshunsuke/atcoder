N = int(input())
d = {}
A = list(map(int, input().split()))
for a in A:
    d[a] = d.get(a, 0) + 1
for i in range(N):
    print(d.get(i + 1, 0))
