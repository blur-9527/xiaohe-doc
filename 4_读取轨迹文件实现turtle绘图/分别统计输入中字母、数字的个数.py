a=input()
b=0
c=0
d=len(a)
for e in range(d):
    f=a[e]
    if(f.isdigit()==True):
        b=b+1
    elif(f.isalpha()==True):
        c=c+1
print(c,b)

