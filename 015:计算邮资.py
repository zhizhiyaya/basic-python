import math
s = input().split()
x, y = int(s[0]), s[1]
sum = 13 if y == 'y' else 8

if x <= 1000:
    print(sum)
else:
    print(math.ceil((x - 1000) / 500) * 4 + sum)
