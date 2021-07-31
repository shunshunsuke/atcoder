import heapq

Q = int(input())
ll = []
heapq.heapify(ll)
sk = 0
for _ in range(Q):
    px = list(map(int, input().split()))
    if px[0] == 1:
        heapq.heappush(ll, px[1] - sk)
    elif px[0] == 2:
        sk += px[1]
    else:
        print(heapq.heappop(ll) + sk)
