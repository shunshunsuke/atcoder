from sys import stdin

s, t = stdin.readline().rstrip().split()
ans = 'Yes' if s < t else 'No'
print(ans)
