from sys import stdin

S = list(stdin.readline().rstrip())
ans = [''.join(S)]
for i in range(1, len(S)):
    tmp = S[i:]
    tmp.extend(S[:i])
    ans.append(''.join(tmp))
ans.sort()
print(ans[0])
print(ans[-1])
