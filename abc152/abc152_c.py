N = int(input())
P = list(map(int, input().split()))
ans = 0
min = float('inf')
for p in P:
    if p <= min:
        ans += 1
        min = p
print(ans)
