N, M = map(int, input().split())
A = list(map(int, input().split()))
sa = set(A)
B = list(map(int, input().split()))
sb = set(B)
A.extend(B)
A.sort()
ans = float('inf')
for i in range(N + M - 1):
    aii = A[i + 1]
    ai = A[i]
    if aii not in sa and ai not in sa:
        continue
    if aii not in sb and ai not in sb:
        continue
    ans = min(ans, aii - ai)
print(ans)
