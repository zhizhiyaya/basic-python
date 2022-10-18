s = input().split()
x, a, b, c, d = float(s[0]),float(s[1]),float(s[2]),float(s[3]),float(s[4])
print( "%.7f" %  (a*x**3 + b*x*x + c*x + d))