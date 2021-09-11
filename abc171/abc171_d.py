from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
Q = int(stdin.readline().rstrip())
ans = sum(A)
t = {}
for a in A:
    t[a] = t.get(a, 0) + 1

for _ in range(Q):
    B, C = [int(x) for x in stdin.readline().rstrip().split()]
    num = t.get(B, 0)
    ans += (C - B) * num
    print(ans)
    t[B] = 0
    t[C] = t.get(C, 0) + num
