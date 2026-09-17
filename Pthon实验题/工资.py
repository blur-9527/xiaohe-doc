a=float(input())
if(a<1000):
    print('{:.2f}'.format(a))
elif(1000<=a<2000):
    print('{:.2f}'.format(0.9*a))
elif(2000<=a<3000):
    print('{:.2f}'.format(0.85*a))
elif(3000<=a<4000):
    print('{:.2f}'.format(0.8*a))
else:
    print('{:.2f}'.format(0.75*a))


