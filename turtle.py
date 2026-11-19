import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.pensize(4)
for i in range(4):
    t.forward(80)
    t.rt(90)
    t.forward(20)
    t.rt(90) 
    t.forward(20)

turtle.mainloop()
