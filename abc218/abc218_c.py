from sys import stdin
import numpy as np

N = int(stdin.readline().rstrip())
S = []
T = []
s_sharp = []
t_sharp = []
st = -1
tt = -1
sb = -1
tb = -1
sl = 300
tl = 300
sr = -1
tr = -1
for h in range(N):
    s = list(stdin.readline().rstrip())
    S.append(s)
    for w in range(len(s)):
        if s[w] == '#':
            sb = h
            if st == -1:
                st = h
            if w < sl:
                sl = w
            if w > sr:
                sr = w

for h in range(N):
    t = list(stdin.readline().rstrip())
    T.append(t)
    for w in range(len(t)):
        if t[w] == '#':
            tb = h
            if tt == -1:
                tt = h
            if w < tl:
                tl = w
            if w > tr:
                tr = w

S = np.array(S)
T = np.array(T)
s_sharp = S[st:sb + 1, sl:sr + 1]
t_sharp = T[tt:tb + 1, tl:tr + 1]
ans = 'No'
if s_sharp.shape == t_sharp.shape and (s_sharp == t_sharp).all():
    ans = 'Yes'
s_90 = np.array(list(zip(*s_sharp))[::-1])
if s_90.shape == t_sharp.shape and (s_90 == t_sharp).all():
    ans = 'Yes'
s_270 = np.array(list(zip(*s_sharp[::-1])))
if s_270.shape == t_sharp.shape and (s_270 == t_sharp).all():
    ans = 'Yes'
s_180 = []
for s_s in s_sharp:
    s_180.append(s_s[::-1])
s_180 = np.array(s_180[::-1])
if s_180.shape == t_sharp.shape and (s_180 == t_sharp).all():
    ans = 'Yes'
print(ans)
