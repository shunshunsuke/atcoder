import math

A, B, H, M = map(int, input().split())
angle_h = 30 * H + M / 2
angle_m = 6 * M
angle = abs(angle_h - angle_m)
co = math.cos(math.radians(angle))
ans = A**2 + B**2 - 2 * A * B * co
print(math.sqrt(ans))
