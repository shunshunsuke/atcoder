Q = int(input())
ll = []
prev = 0
pn = 0
for _ in range(Q):
    px = list(map(int, input().split()))
    if px[0] == 1:
        ll.append(px[1])
    elif px[0] == 2:
        pn += px[1]
    else:
        if prev != 3:
            ll.sort(reverse=True)
            ll = list(map(lambda x: x + pn, ll))
            pn = 0
        print(ll.pop(-1))
    prev = px[0]
