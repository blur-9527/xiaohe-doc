a=int(input())
for i in range(100,a+1):
    b=str(i)
    c=int(b[0])
    d=int(b[1])
    e=int(b[2])
    f=c*c*c+d*d*d+e*e*e
    if(i==f):
        print(i)


