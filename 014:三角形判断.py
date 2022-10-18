# 任意两边之和大于第三边，任意两边之差小于第三边
s = input().split()
x, y, z = int(s[0]), int(s[1]), int(s[2])

if x + y > z and x + z > y and y + z > x and abs(x - y) < z and abs(x - z) < y and abs(y - z) < x:
    print('yes')
else:
     print('no')