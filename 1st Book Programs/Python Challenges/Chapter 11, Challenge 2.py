import turtle
t = turtle.Pen()
def myoctagon(size, filled):
	if filled == True:
		t.begin_fill()
	for x in range(1, 9):
		t.forward(size)
		t.left(45)
	if filled == True:
		t.end_fill()

t.color(0.9, 0.75, 0)
myoctagon(50, True)
t.color(0, 0, 0)
myoctagon(50, False)
