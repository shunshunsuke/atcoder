from sys import stdin
import array

N = int(stdin.readline().rstrip())
S = [int(x) for x in stdin.readline().rstrip().split()]
T = [int(x) for x in stdin.readline().rstrip().split()]

ans = array.array('i', [10 ** 9 + 1] * N)
for i in [i[0] for i in sorted(enumerate(T), key=lambda x:x[1])]:
    t = T[i]
    j = i
    while True:
        if t < ans[j]:
            ans[j] = t
            t += S[j]
            if j == N - 1:
                j = 0
            else:
                j += 1
        else:
            break

for a in ans:
    print(a)
