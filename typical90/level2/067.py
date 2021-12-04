from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
x = N
for i in range(K):
    ret = ''
    n_10 = int(str(x), 8)
    n_9 = ''
    y = n_10
    while True:
        d, m = divmod(y, 9)
        n_9 = str(m) + n_9
        y = d
        if d < 9:
            n_9 = str(d) + n_9
            break
    x = n_9.replace('8', '5')
print(int(x))
