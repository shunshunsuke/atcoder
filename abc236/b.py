import collections
from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
for item in collections.Counter(A).items():
    if item[1] != 4:
        print(item[0])
        break
