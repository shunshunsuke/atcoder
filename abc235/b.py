from sys import stdin

N = int(stdin.readline().rstrip())
H = [int(x) for x in stdin.readline().rstrip().split()]
ans = H[0]
for i in range(1, N):
    if H[i] > ans:
        ans = H[i]
    else:
        break
print(ans)
