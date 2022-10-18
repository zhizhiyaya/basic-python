s = input().split()
x, y, sign = int(s[0]), int(s[1]), s[2]
if sign == '+':
    print(x + y)
elif sign == '-':
    print(x - y)
elif sign == '*':
    print(x * y)
elif sign == '/':
    if y == 0:
        print('Divided by zero!')
    else:
        print(int(x / y))
else:
    print('Invalid operator!')