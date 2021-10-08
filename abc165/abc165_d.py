from sys import stdin
import math

A, B, N = [int(x) for x in stdin.readline().rstrip().split()]
x = min(N, B - 1)
print(math.floor((A * x) / B) - A * math.floor(x / B))
