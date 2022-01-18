from sys import stdin

N = int(stdin.readline().rstrip())
abc = [int(x) for x in stdin.readline().rstrip().split()]
abc.sort(reverse=True)
A, B, C = abc
ans = 10001
for x in range(N // A + 1):
    yy = N - A * x
    for y in range(yy // B + 1):
        zz = yy - B * y
        if zz % C == 0:
            ans = min(ans, x + y + zz // C)
print(ans)
