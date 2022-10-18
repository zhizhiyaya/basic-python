import math

s = input().split()
h, r = int(s[0]), int(s[1])
v = math.pi * r * r * h / 1000;

print(math.ceil(20 / v))