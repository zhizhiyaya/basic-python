n = int(input())
list = [0, 0, 0]
for i in range(n):
    a = input().split()
    for j in range(3):
        list[j] = list[j] + int(a[j])

print("%d %d %d %d" % (list[0], list[1], list[2], list[0] + list[1] + list[2]))
