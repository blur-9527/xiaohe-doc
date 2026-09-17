a=int(input())
c=1
if(a<=1):
    print(0)
elif(a==2):
    print(1)
else:
    for b in range(2,a):
        if(a%b==0):
            c=0
            break
    if(c==0):
        print(c)
    else:
        print(1)

