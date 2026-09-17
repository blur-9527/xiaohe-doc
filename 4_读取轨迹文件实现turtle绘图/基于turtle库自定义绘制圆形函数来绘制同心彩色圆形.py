def a(b,c,d,e,f,g):
    import turtle as h
    h.penup()
    h.goto(b,c-d)
    h.pendown()
    h.fillcolor(e)
    h.begin_fill()
    h.circle(d)
    h.end_fill()
i=["purple","red","blue","yellow","orange","coral","brown","yellow","fuchsia"]
for j in range(1,10):
    k=10-j
    l=k-1
    a(0,0,k*10,i[l],0,0)
    



