N = int(input())
X = list(map(int, input().split()))
ans = float('inf')
for i in range(1, 101):
    s = 0
    for x in X:
        s += (x - i)**2
    if s < ans:
        ans = s
print(ans)
