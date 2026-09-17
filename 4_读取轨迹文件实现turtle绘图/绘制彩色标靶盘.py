import turtle as a
c=["purple","red","blue","yellow","orange","coral","brown","yellow","fuchsia"]
for b in range(1,10):
    d=10-b
    e=d-1
    a.penup()
    a.goto(0,b*10)
    a.pendown()
    a.fillcolor(c[e])
    a.begin_fill()
    a.circle(d*10)
    a.end_fill()

