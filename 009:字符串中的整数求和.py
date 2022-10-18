s = input()
a = s.split()
sum = 0
for i in a:
    sum += int(i[:2])
print(sum)