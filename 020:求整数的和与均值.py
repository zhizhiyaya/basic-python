n = int(input())
sum = 0;
for i in range(0, n):
    sum += int(input())
print("%d %.5f" % (sum, (sum / n)))
