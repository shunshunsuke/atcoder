from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
ranking = []
sums = []
for i in range(N):
    s = sum([int(x) for x in stdin.readline().rstrip().split()])
    ranking.append(s)
    sums.append(s)
ranking.sort(reverse=True)
for i in range(N):
    s = sums[i]
    if s + 300 >= ranking[K - 1]:
        print('Yes')
    else:
        print('No')
