def sum(n):
    if n==1 or n==2:
        return 1
    else:
        return sum(n-1)+sum(n-2)
x=int(input())
a=sum(x)
print(a)


