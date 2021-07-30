N = int(input())
A = list(map(int, input().split()))
ans = 0
prev = A[0]
for i in range(1, N):
    if prev > A[i]:
        ans += prev - A[i]
    else:
        prev = A[i]
print(ans)
