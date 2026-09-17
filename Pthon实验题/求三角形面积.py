import math

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

s = (a+b+c)/2
sum = float(s*(s-a)*(s-b)*(s-c))
ans = math.sqrt(sum)

print("{:.3f}".format(ans))

