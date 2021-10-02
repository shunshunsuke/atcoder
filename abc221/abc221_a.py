from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]

print(32 ** (a - b))
