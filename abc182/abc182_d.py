from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
sum_a = 0
pos = 0
max_pos = 0
ans = 0
for i in range(N):
    sum_a += A[i]
    max_pos = max(sum_a, max_pos)
    tmp_max = pos + max_pos
    ans = max(tmp_max, ans)
    pos += sum_a
print(ans)
