from sys import stdin

abc = stdin.readline().rstrip()
bca = int(abc[1] + abc[2] + abc[0])
cab = int(abc[2] + abc[0] + abc[1])
print(int(abc) + bca + cab)
