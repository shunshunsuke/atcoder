from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
target = sum(A)
A.extend(A[:-1])
total = 0
si = 0
for i in range(2 * N - 1):
    total += A[i]
    if 10 * total > target:
        total -= A[si]
        si += 1
    elif 10 * total == target:
        print('Yes')
        exit()
print('No')
