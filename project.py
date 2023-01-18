from turtle import *  # import
import turtle
import time


def square(l=100):  # function in one argument
    for i in range(4):  # loop run 0 to 3 range
        t.forward(l)   # draw forward line
        t.left(90)  # farward line after 90 degree ya 90 band


def cube(l, a):  # function in two argument
    square(l)  # call sqare function
    # time.sleep(2)
    t.left(a)  # farward line after a value band

    t.forward(l)  # draw forward line
    # time.sleep(2)
    t.right(a)
    # time.sleep(2)
    square(l)
    t.left(60+a)  # band line angle left side angle
    t.forward(l)  # draw forward line
    t.right(30+a)  # band line angle right side angle
    t.backward(l)  # draw backward line
    t.right(a)  # band line angle right side angle
    t.forward(l)  # draw forward line
    t.left(a)  # band line angle left side angle
    t.forward(l)  # draw forward line
    t.right(90+a)  # band line angle right side angle
    t.forward(l)  # draw forward line
    t.right(30+a)  # band line angle right side angle
    t.forward(l)  # draw forward line
    turtle.done()  # .done method mean stop pattern and show

# t.end_fill()


shapes = ['square', 'circle', 'rectangle', 'star', 'circlestyle',
          '3dcube']  # create list and all element shape name shore
print('show all shape name')
for a in shapes:  # use for show all data help of loop
    # a mean show element  and  end equal to mean do not break line continue after space
    print(a, ",", end="   ")

print()
shapeName = input("enter shape name   :")  # enter space from user
# one exception user enter somer letter is capital or some is lower case
shapeName = shapeName.lower()


# check input equal to shape is square or condition is true is mean show square shape and logical or operator
if (shapeName == "square" or shapeName == '1'):
    lincolor = input("enter line color   :")   # enter which of line
    fillcolo = input("enter fill color   :")    # enter which of color is fill

    wn = turtle.Screen()    # show screen in python
    # screen back ground color is write in bracket inside
    wn.bgcolor('light green')
    wn.title("square ")  # show shape title

    s = turtle.Turtle()  # control on screen
    s.begin_fill()  # any color fill in shape
    s.pensize(10)  # pen size mean line size
    s.color(lincolor, fillcolo)  # mean which color
    for i in range(4):  # run for loop four time
        s.forward(100)  # forward drawn line and line length is  100
        s.right(90)  # angle right side in 90 degree
    s.end_fill()   # fill color in shape

    turtle.done()  # stop run after the shape show
    # all method that before all method  is define is use in below
elif (shapeName == "circle" or shapeName == '2'):
    wn = turtle.Screen()  # create  screen method
    wn.bgcolor('light green')  # change background color
    wn.title("Draw circle")  # title of page
    s = turtle.Turtle()   # screen control
    s.begin_fill()      # fill start begin to between all shape color fill
    # first color is line color and second is background color
    s.color('blue', 'cyan')
    s.speed(100)  # control the speed of shape
    s.pensize(5)  # size of line

    for i in range(100):    # run loop
        s.forward(5)        # drawn forward line
        s.right(5)          # define agle right side 5 degree
    s.end_fill()  # fill color method is end
    turtle.done()  # end of the sreen is done show only
# condition check enter rectangle and 3 show rectangle
elif (shapeName == "rectangle" or shapeName == '3'):
    wn = turtle.Screen()   # create screen
    wn.bgcolor('light green')  # fill background color
    wn.title("draw rectangle")

    s = turtle.Turtle()   # control screen for write line of pattarn
    s.begin_fill()      # fill color of begin fill method
    s.pensize(10)       # define line size
    # color method is use first color is line color and second is inside color
    s.color('black', 'gray')
    for i in range(4):      # iterate the loop 4 times
        if (i == 1 or i == 3):  # main condition of rectangle
            s.forward(100)         # drawn forward line length is 100
            # drawn the angle of line right side of 90 degree
            s.right(90)
        else:            # condition is false is run this condition
            s.forward(200)    # draw forward line 100 length
            s.right(90)      # draw line angle is 90 right side
    s.end_fill()            # end of color fill
    turtle.done()            # done mean only show screen
elif (shapeName == 'star' or shapeName == '4'):    # enter star or 4 mean condition is true
    wn = turtle.Screen()   # create screen
    wn.bgcolor('light green')  # fill background color
    wn.title("Draw star")   # title of screen
    s = turtle.Turtle()     # create control of screen on control
    s.begin_fill()         # color fill on begin
    s.pensize(10)         # define pen size mean line size
    # first is line color  and second is which shape is fill
    s.color('black', 'orange')
    s.speed(1)      # speed drawn shape speed

    for i in range(5):    # iterate loop 5 time
        s.forward(200)    # drawn line 200 forward
        s.right(144)      # show angle of right side
    s.end_fill()  # end of color is fill
    turtle.done()       # done method mean stop

elif (shapeName == 'circlestyle' or shapeName == '5'):   # write  circlestyle  or 5
    wn = turtle.Screen()    # create of screen
    wn.bgcolor('light green')   # mean bg color of shape
    wn.title(" drawn circlestyle ")  # write the title of image
    s = turtle.Turtle()      # control on screen
    s.begin_fill()          # color fill begin of color
    s.pensize(2)             # pen size mean line size
    # color method is use for first is line color and second is which color is fill
    s.color('green', 'green')
    s.speed(100)        # mean line of speed of shape
    for i in range(50):    # iterate the loop number of range that define in range function
        s.forward(100)  # forward line draw that define in forward method
        s.right(250)        # angle of right side move

    end_fill()                 # fill color of end_fill function
    turtle.done()               # done turtle of done method

elif (shapeName == '3dcube' or shapeName == '6'):  # enter input if 3dcube or 6 condition true
    # emter the length of line in integer value
    l = int(input("enter the length of lines     :"))
    a = 30       # that define angle is constant
    t = turtle.Turtle()
    s = turtle.Screen()
    #    t.begin_fill()
    t.color('red')     # color mean fill

    s.title('3d cube  ')   # title name of shape name

    # define size of screen size 800 by 500 and background color
    s.screensize(800, 500, bg='black')
    # t.pencolor('white')
    t.pensize(3)   # define size of line
    cube(l, a)   # two argument function
else:
    print('please enter rigth shape name that in start')


