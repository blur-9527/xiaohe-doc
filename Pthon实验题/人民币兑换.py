x=float(input())
ten=int(x/10)
five=int(x%10/5)
two=int((x-ten*10-five*5)/2)
one=int((x-ten*10-five*5-two*2)/1)
print(ten,five,two,one,end=" ")

