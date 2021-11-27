from sys import stdin

A, B = stdin.readline().rstrip().split()
A = list(A)
B = list(B)
A.reverse()
B.reverse()
for i in range(len(A)):
    if i >= len(B):
        break
    if int(A[i]) + int(B[i]) >= 10:
        print('Hard')
        exit()
print('Easy')
