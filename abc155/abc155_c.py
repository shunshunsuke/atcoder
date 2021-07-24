N = int(input())
d = {}
for _ in range(N):
    s = input()
    d[s] = d.get(s, 0) + 1

dl = sorted(d.items(), key=lambda x: (-x[1], x[0]))
max = dl[0][1]
for d in dl:
    if d[1] < max:
        break
    print(d[0])
