s = input()
n = int(s)
if n < 0:
    s1 = s[-1:0:-1]
else:
    s1 = s[-1::-1]
r = ""
for c in s1:
    r += str(c);
r = int(r)

if n < 0:
    r = '-' + str(r)
print(r)

