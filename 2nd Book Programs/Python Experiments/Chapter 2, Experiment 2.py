# make a house
import turtle
turtle.bgcolor('blue')
shelly = turtle.Turtle()
# make the first big square for house
shelly.begin_fill() # start fill of color
shelly.color('gray')
for i in range(4):
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill() # end fill of color
shelly.penup()
shelly.goto(-20, 100) # move turtle to next area
shelly.pendown()
# make a red triangle roof
shelly.begin_fill() # start fill for roof
shelly.color('red')
shelly.left(60)
for x in range(2):
    shelly.forward(140)
    shelly.right(120)
shelly.forward(140)
shelly.end_fill() # end fill of color for roof
# make a window
shelly.penup()
shelly.goto(25, 80) # move to window
shelly.pendown()
shelly.begin_fill() # start filling window color
shelly.color('yellow')
for j in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill() # end filling window color
# hide the turtle when done
shelly.hideturtle()














