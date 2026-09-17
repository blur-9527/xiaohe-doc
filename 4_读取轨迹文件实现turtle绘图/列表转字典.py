a=list(input().split(","))
b=list(input().split(","))
c=int(input())
d=zip(a,b)
e=dict(d)
g=a[c]
f=e.get(g)
print(f)


