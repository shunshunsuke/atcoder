import math
from decimal import Decimal

A, B = map(Decimal, input().split())
print(math.floor(A * B))
