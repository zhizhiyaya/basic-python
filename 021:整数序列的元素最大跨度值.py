n = int(input())
s = input().split()
if len(s) == 0:
    print(0)
minNum = int(s[0])
maxNum = int(s[0])
for i in s[1:n]:
    i = int(i)
    if i < minNum:
        minNum = i
    elif i > maxNum:
        maxNum = i
print(maxNum - minNum)
