import turtle
import linecache as c
for b in range(2,9):
    d=c.getline("turtledata.txt",b)
    f=d[:-1]
    e=f.split(",")
    e=list(map(int,e))
    if(e[0]==0):
        turtle.left(e[1])
    else:
        turtle.right(e[1])
    turtle.colormode(255)
    turtle.color(e[3],e[4],e[5])
    turtle.pensize(e[6])
    turtle.forward(e[2])
    


