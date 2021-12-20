from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
C = []
for _ in range(H):
    c = stdin.readline().rstrip()
    C.append(list(c))
stack = [[0, 0, 1]]
ans = 0
while len(stack) > 0:
    x, y, d = stack.pop()
    ans = max(ans, d)
    if ans == H + W - 1:
        break
    if x < H - 1:
        if C[x + 1][y] == '.':
            stack.append([x + 1, y, d + 1])
    if y < W - 1:
        if C[x][y + 1] == '.':
            stack.append([x, y + 1, d + 1])
print(ans)
