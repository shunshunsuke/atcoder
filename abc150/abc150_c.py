import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

l = list(itertools.permutations(list(range(1, N + 1)), N))
print(abs(l.index(tuple(P)) - l.index(tuple(Q))))
