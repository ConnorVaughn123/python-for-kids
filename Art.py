# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 36 hexagons, each 90 degrees apart
for n in range(36):
# make hexagon by repeating 6 times
 for i in range(6):
    shelly.color(colors[i]) # pick color at position i
    shelly.forward(100)
    shelly.left(60)
# add a turn before the next hexagon
 shelly.right(10)
