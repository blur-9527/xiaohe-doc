a,b=input().split(":")
c=int(a)
d=int(b)
e=c*30+d*0.5
f=d*6
g=e-f
if(g<0 and g>-180):
    g=0-g
elif(g>360):
    g=g-360
elif(g>180 and g<=360):
    g=360-g
print("{:.3f}".format(g))

