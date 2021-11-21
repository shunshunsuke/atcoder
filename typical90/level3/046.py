from sys import stdin

def set_num(arr):
    nums = {}
    for x in arr:
        t = x % 46
        v = nums.get(t, 0)
        nums[t] = v + 1
    return nums

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
C = [int(x) for x in stdin.readline().rstrip().split()]

num_a, num_b, num_c = set_num(A), set_num(B), set_num(C)
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += num_a.get(i, 0) * num_b.get(j, 0) * num_c.get(k, 0)
print(ans)
