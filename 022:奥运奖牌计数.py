n = int(input())
list = [0, 0, 0]
for i in range(0, n):
    a = input().split()
    for (j,n) in list:
        print(j, n)
        list[n] = j + int(a[j])

print("%d %d %d %d" % (list[0], list[1], list[2], list[0] + list[1] + list[2]))
