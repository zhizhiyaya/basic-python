s = input()
len = len(s)
r = ''
for i in range(-1, -len-1, -1):
    r += s[i]
print(r)