a,b,c=input().split(".")
d,e,f=input().split(".")
A=int(a)
B=int(b)
C=int(c)
D=int(d)
E=int(e)
F=int(f)
G=D-A
if(E<B):
    G=G-1
elif(E==B and F<C):
    G=G-1
print(G)    

