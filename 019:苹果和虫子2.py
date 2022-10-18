import math
s = input().split()
n, x, y = int(s[0]), int(s[1]), int(s[2])
r = n - math.ceil(y / x)
if r < 0:
    r = 0

print(r)