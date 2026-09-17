a=input()
b=[]
c=len(a)
for d in  range(c):
    e=a[d]
    f=len(b)
    i=1
    for g in range(f):
        h=b[g]
        if(h==e):
            i=0
    if(i==0):
        pass
    else:
        b.append(e)
j="".join(b)
print(j)

