a,b,c=input().split()
d=int(a)
e=int(b)
if(c=="*"):
    print(d*e)
elif(c=="+"):
    print(d+e)
elif(c=="-"):
    print(d-e)
elif(c=="/"and d%e==0):
    print(int(d/e))
else:
    print('{:.2f}'.format(d/e))
    

