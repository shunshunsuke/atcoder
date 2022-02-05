from sys import stdin

def digit_sum(x):
    # 各桁の和を求める
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

N, K = [int(x) for x in stdin.readline().rstrip().split()]
mod = 100000
# ボタンを1回押した後の値を保持する
nxt = [0] * mod
for i in range(mod):
    nxt[i] = (i + digit_sum(i)) % mod
time_stamp = [-1] * mod
pos = N
cnt = 0
# 既に表示済みの値が登場するまで実行して1ループを求める
while time_stamp[pos] == -1:
    time_stamp[pos] = cnt
    pos = nxt[pos]
    cnt += 1
cycle = cnt - time_stamp[pos]
if K >= time_stamp[pos]:
    K = (K - time_stamp[pos]) % cycle + time_stamp[pos]
answer = -1
for i in range(mod):
    if time_stamp[i] == K:
        answer = i
print(answer)
