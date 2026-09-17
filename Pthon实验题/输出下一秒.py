#输出当前时间下一秒
h,min,sec=input().split(":")

sec1=int(sec)
min1=int(min)
h1=int(h)

sec1+=1

if(sec1==60):
    min1+=1
    sec1=0
    if(min1==60):
       h1+=1
       min1=0
       if(h1==24):
          h1=0

print(h1,min1,sec1,sep=":")


