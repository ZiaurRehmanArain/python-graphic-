# import turtle
# wn= turtle.Screen()
# wn.bgcolor('light green')
# wn.title("my first test of grapic window")
# s=turtle.Turtle()
# for i in range(4):
#     s.forward(50)
#     s.right(90)

# turtle.done()

# import turtle
# wn= turtle.Screen()
# wn.bgcolor('light green')
# wn.title("my first test of grapic window")
# # wn.speed(0)
# s=turtle.Turtle()
# s.color('blue','red')
# s.speed(100)

# for i in range(100):
#     s.forward(50)
#     s.right(50)
    
# turtle.done()

# # # # # # # 7 side squre

# import turtle
# wn= turtle.Screen()
# wn.bgcolor('light green')
# wn.title("my first test of grapic window")
# # wn.speed(0)
# s=turtle.Turtle()
# s.color('blue','cyan')
# s.speed(100)

# for i in range(100):
#     s.forward(5)
#     s.right(5)
    
# turtle.done()




# import turtle
# wn= turtle.Screen()
# wn.bgcolor('light green')
# wn.title("my first test of grapic window")
# # wn.speed(0)
# s=turtle.Turtle()
# s.color('blue','cyan')
# s.speed(1)

# for i in range(5):
#     s.forward(50)
#     s.right(144)
    
# turtle.done()


# # # # # # # change shape

# from turtle import *
# import turtle
# wn= turtle.Screen()
# wn.bgcolor('light green')
# wn.title("my first test of grapic window")
# s=turtle.Turtle()
# s.color('brown','black')
# begin_fill()
# s.speed(100)

# for i in range(50):
#     s.forward(100)
#     s.right(250)
    
# end_fill()
# turtle.done()




# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()



# # # # # /////////////////////////////

# # # # # 3d cube


# from turtle import *
# import turtle
# import time
# l=int(input("enter the length"))
# a=30
# t= turtle.Turtle()
# s=turtle.Screen()
# # t.begin_fill()
# t.color('red')

# s.title('3d cube  ')

# s.screensize(800,500,bg='black')
# # t.pencolor('white') 
# t.pensize(3)
# # t.fillcolor('green')
# # turtle.pos()(0.00, 240.00)
# def square(l=100):
#     for i in range(4):
#         t.forward(l)
#         t.left(90)
    

# def cube(l,a):
#  square(l)
#  # time.sleep(2)
#  t.left(a)

#  t.forward(l)
#  # time.sleep(2)
#  t.right(a)
#  # time.sleep(2)
#  square(l)
#  t.left(60+a)
#  t.forward(l)
#  t.right(30+a)
#  t.backward(l)
#  t.right(a)
#  t.forward(l)
#  t.left(a)
#  t.forward(l)
#  t.right(90+a)
#  t.forward(l)
#  t.right(30+a)
#  t.forward(l)

# cube(l,a)
# # t.end_fill()
# turtle.done()





# # # # square and fill color

# from turtle import *

# drawing_area = Screen()
# drawing_area.setup(width=750, height=500)

# width(10)


# def draw_rectangle(linecolor, length1=100, length2=150):
#     color(linecolor,'green')
#     for i in range(2):
#         forward(length1)
#         left(90)
#         forward(length2)
#         left(90)


# begin_fill()
# draw_rectangle('red')
# end_fill()

# done()