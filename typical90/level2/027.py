from sys import stdin

N = int(stdin.readline().rstrip())
names = {}
for i in range(N):
    s = stdin.readline().rstrip()
    exists = names.get(s, False)
    if not exists:
        print(i + 1)
        names[s] = True
