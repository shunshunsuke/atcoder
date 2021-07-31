X = input()
if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    print('Weak')
else:
    ans = 'Weak'
    for i in range(3):
        if not (int(X[i + 1]) - int(X[i]) == 1 or int(X[i + 1]) - int(X[i]) == -9):
            ans = 'Strong'
    print(ans)
