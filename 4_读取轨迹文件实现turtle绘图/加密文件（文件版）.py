import os
c=input()
d=len(c)
e={}
m=97
for f in range(d):
    g=c[f]
    j=0
    for h in range(f):
        i=c[h]
        if(i==g):
            j=1
    if(j==0):
        k=chr(m)
        m=m+1
        l={k:g}
        e.update(l)
for n in range(122,96,-1):
    o=chr(n)
    j=0
    for p in range(d):
        g=c[p]
        if(o==g):
            j=1
    if(j==0):
        k=chr(m)
        m=m+1
        l={k:o}
        e.update(l)
a=open("encrypt.txt")
b=a.read()
q=len(b)
s=""
for r in range(q):
    g=b[r]
    if(g.isalpha()==True):
        s=s+e.get(g)
    else:
        s=s+g
u=open("output.txt","w+")
u.write(s)


