# Lab03avst.py
# This program draws a colored house with turtle graphics.
# Evin Lodder 10/21
from turtle import *
from math import sin, radians
from random import randint


# Draw rectangle with specified x, y, width, height, fill color, border color, and bools for centering
def draw_rec(x: float,
             y: float,
             width: float,
             height: float,
             fcol: str,
             bcol: str,
             centx: bool = True,
             centy: bool = False) -> None:
    penup()
    if centx:
        x -= width / 2
    if centy:
        y -= height / 2
    goto(x, y)
    color(bcol)
    fillcolor(fcol)
    begin_fill()
    pendown()
    for i in range(2):
        fd(width)
        left(90)
        fd(height)
        left(90)
    end_fill()


# Draw triangle with specified x, y, length, angles, fill color, border color, and bools for centering
def draw_tri(x: float,
             y: float,
             length: float,
             angles: list[float],
             fcol: str,
             bcol: str,
             centx: bool = True,
             centy: bool = False) -> None:
    penup()
    if centx:
        x -= length / 2
    if centy:
        y -= length / 2
    goto(x, y)
    color(bcol)
    fillcolor(fcol)
    begin_fill()
    pendown()
    ratio: float = length / (sin(radians(angles[1])))
    b: float = ratio * sin(radians(angles[0]))
    c: float = ratio * sin(radians(angles[2]))
    lengths: list[float] = [length, b, c]
    for i in range(3):
        fd(lengths[i])
        left(180 - angles[i])
    end_fill()


def draw_rec_window(x: float, y: float, width: float, height: float) -> None:
    draw_rec(x, y - height, width, height, "white", "black", False)
    penup()
    goto(x, y - height / 2)
    pendown()
    setheading(0)
    fd(width)
    penup()
    goto(x + width / 2, y)
    pendown()
    setheading(270)
    fd(height)
    penup()
    setheading(0)


# Settings used for entire program
tracer(0,0)
hideturtle()
width(2)

# Background
draw_rec(-1000, -125, 2000, 800, "light blue", "light blue", False)
draw_rec(-1000, -625, 2000, 500, "green", "green", False)

# Chimney
draw_rec(-100, 100, 50, 200, "gray", "black")

# Smoke
penup()
for i in range(10):
    goto(-randint(80, 110), randint(315, 450))
    dot(randint(10, 40), "antiquewhite3")

# Draw roof
draw_tri(-25, 125, 550, [30, 120, 30], "maroon", "black")

# Draw base rectangle segment
draw_rec(-225, 0, 400, 250, "burlywood", "black", centx=False, centy=True)
# Bricks
width(1)
penup()
right(90)
for j in range(10):
    color("black")
    # First row of bricks
    for i in range(-225, 185, 20):
        goto(i, 125 - j * 25)
        pendown()
        fd(12.5)
        penup()
    # Separating line between layers
    goto(-225, (112.5 - j * 25))
    pendown()
    left(90)
    fd(400)
    right(90)
    penup()
    # Second row of bricks
    for g in range(-215, 175, 20):
        goto(g, 112.5 - j * 25)
        pendown()
        fd(12.5)
        penup()
    # Second separating line to complete 2-brick-tall row
    goto(-225, (100 - j * 25))
    pendown()
    left(90)
    fd(400)
    right(90)
    penup()

# Reset rotation and width
left(90)
width(2)

# Garage
draw_rec(-100, -125, 200, 125, "sienna", "black")
draw_rec(-100, -110, 50, 2, "black", "black")

# Draw door
penup()
draw_rec(65, -125, 50, 80, "brown", "black", centx=False)
penup()
goto(100, -90)
pendown()
dot(10, "gold")
penup()
# Draw circle window
penup()
goto(90, -20)
pendown()

# Fill window circle
fillcolor("white")
begin_fill()
circle(25)
end_fill()

# Draw lines
penup()
goto(90, 30)
pendown()
setheading(270)
fd(50)
penup()

goto(65, 5)
pendown()
setheading(0)
fd(50)
penup()


# Draw top-center window
draw_rec_window(-75, 100, 75, 50)

# Draw top-left window
draw_rec_window(-200, 100, 75, 50)

# Draw top-right window
draw_rec_window(50, 100, 75, 50)

# Draw bottom-left window
draw_rec_window(20, -50, 30, 30)

# Draw bottom-right window
draw_rec_window(130, -50, 30, 30)

update()
done()
