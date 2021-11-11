from sys import stdin
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

x = Decimal(float(stdin.readline().rstrip())).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(x)
