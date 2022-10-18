import math
c = input()
n = 7
sub = math.ceil(n / 2)
i = 1
step = 2
for i in range(1, n, step):
    print(" " * (sub - 1 - int((i + 1) / 2))  + c * i)

