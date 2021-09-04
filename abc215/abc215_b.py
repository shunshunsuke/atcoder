from sys import stdin

N = int(stdin.readline().rstrip())
k = 1
while 2**k <= N:
    k += 1
print(k - 1)
