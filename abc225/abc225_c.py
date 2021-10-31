from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
next_b = []
for _ in range(N):
    b = [int(x) for x in stdin.readline().rstrip().split()]
    if len(next_b) == 0:
        for i in range(len(b) - 1):
            if b[i + 1] - b[i] != 1:
                print('No')
                exit()
            if b[i] % 7 == 0:
                print('No')
                exit()
            if b[i] % 7 == 6:
                if b[i + 1] % 7 != 0:
                    print('No')
                    exit()
            elif (b[i + 1] % 7) - (b[i] % 7) != 1:
                print('No')
                exit()
    else:
        if b != next_b:
            print('No')
            exit()
    next_b = list(map(lambda x: x + 7, b))


print('Yes')
