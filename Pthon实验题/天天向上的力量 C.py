n = float(input())*0.001
i = j = 0
x = y = 1.0

while i < 365:
    x *= 1+n
    i += 1

while j < 365:
    y *= 1-n
    j += 1

z = x/y

print("{:.2f},{:.2f},{:.0f}".format(x, y, z))

