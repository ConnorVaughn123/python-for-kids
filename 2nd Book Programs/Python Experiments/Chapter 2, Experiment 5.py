import turtle
shelly = turtle.Turtle()
turtle.speed(fastest)
turtle.bgcolor('black')
shelly.color('white')
for i in range(36):
    shelly.penup()
    shelly.forward(200)
    for j in range(6):
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.backward(20)
    shelly.backward(80)
    shelly.right(10)
shelly.hideturtle()
