from sys import stdin

N = int(stdin.readline().rstrip())
s = set()
for _ in range(N):
    LA = stdin.readline().rstrip()
    s.add(LA)
print(len(s))
