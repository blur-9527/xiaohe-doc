x=list(map(int,input().split(',')))
y=x.copy()
odd=1
for i in range(len(y)):
    if i%2 == 0:
        y[i] = odd
        odd += 2
print(x)
print(y)

