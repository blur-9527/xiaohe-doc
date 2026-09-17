a=int(input())
c=0
for b in range(1,a+1):
    c=c+(1/(2*b-1)*(-1)**b)
d=4*c
d=0-d
print("{:.8f}".format(d))

