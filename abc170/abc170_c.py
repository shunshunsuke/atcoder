X, N = map(int, input().split())
P = list(map(int, input().split()))
diff = 0
while True:
    if not X - diff in P:
        print(X - diff)
        break
    elif not X + diff in P:
        print(X + diff)
        break
    else:
        diff += 1
