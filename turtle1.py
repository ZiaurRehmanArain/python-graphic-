import turtle 
s=turtle.Turtle()
a=turtle.Screen()
s.begin_fill()
s.setheading(90)
a.bgcolor("green")
# s.color("yellow",'yellow')
s.color("yellow",'blue')
# s.fillcolor("blue")
s.pensize(10)
s.shape('turtle')
s.penup()
s.goto(10,-100)
s.pendown()
# turtle.fillcolor('blue')
for a in range(4):

    s.forward(100)
    s.left(90)
s.end_fill()

turtle.done()     


# import turtle
# t = turtle.getscreen()
# t =turtle.Turtle() 
# t.shapesize(3,3,3) 
# t.fillcolor("blue") 
# turtle.mainloop() 
# turtle.done()        