def a(b):
    c=1
    if(b<=1):
        print(0)
    elif(b==2):
        print(1)
    else:
        for d in range(2,b):
            if(b%d==0):
                c=0
                break
        if(c==0):
            print(0)
        else:
            print(1)
e=int(input())
f=a(e)



    


