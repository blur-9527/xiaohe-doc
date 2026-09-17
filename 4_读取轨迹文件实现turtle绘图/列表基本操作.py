a=list(input().split(" "))
b=list(input().split(" "))
c=a+b
d=len(c)
c.insert(d,"123")
c.pop(0)
c=list(map(int,c))
print(c)


