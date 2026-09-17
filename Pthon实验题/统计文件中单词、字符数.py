a=open("in.txt")
b=a.read()
c=len(b)
f=0
g=0
for d in range(c):
    e=b[d]
    if(e.isalpha()==True and f==0):
        g=g+1
        f=1
    elif(e.isalpha()==True and f==1):
        pass
    else:
        f=0
print(g,c-1)
        


