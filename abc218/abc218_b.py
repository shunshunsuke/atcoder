from sys import stdin

p = [int(x) for x in stdin.readline().rstrip().split()]
abc = list('abcdefghijklmnopqrstuvwxyz')
ans = ''
for i in p:
    ans += abc[i - 1]
print(ans)
