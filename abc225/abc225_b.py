from sys import stdin

N = int(stdin.readline().rstrip())
AB = []
for _ in range(N - 1):
    ab = [int(x) for x in stdin.readline().rstrip().split()]
    AB.append(ab)

a0, b0 = AB[0]
a1, b1 = AB[1]
star = 0
if a0 == a1 or a0 == b1:
    star = a0
elif b0 == a1 or b0 == b1:
    star = b0
else:
    print('No')
    exit()

for ab in AB:
    a, b = ab
    if a != star and b != star:
        print('No')
        exit()
print('Yes')
