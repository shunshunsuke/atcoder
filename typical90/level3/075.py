import math
from sys import stdin

N = int(stdin.readline().rstrip())
a = 2
num = 0
while a * a <= N:
    if N % a != 0:
        a += 1
        continue
    ex = 0
    while N % a == 0:
        ex += 1
        N /= a
    num += ex
    a += 1
if N != 1:
    num += 1

print(math.ceil(math.log2(num)))
