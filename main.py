# Lab03avst.py
# This program draws a colored house with turtle graphics.
# Evin Lodder 10/19
from turtle import *
from math import sin, radians
def draw_rec(x: float, y: float, width: float, height: float, fcol: str, bcol: str, centx: bool = True, centy: bool = False) -> None:
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
def draw_iso_tri(x: float, y: float, length: float, fcol: str, bcol: str, centx: bool = True, centy: bool = False):
    draw_tri(x, y, length, [60, 60, 60], fcol, bcol, centx, centy)
def draw_tri(x: float, y: float, length: float, angles: list[float], fcol: str, bcol: str, centx: bool = True, centy: bool = False):
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
    print(f"{ratio=}")
    b: float = ratio * sin(radians(angles[0]))
    print(f"{b=}")
    c: float = ratio * sin(radians(angles[2]))
    print(f"{c=}")
    lengths: list[float] = [length, b, c]
    for i in range(3):
        fd(lengths[i])
        left(180 - angles[i])
        print(f"going {lengths[i]} turning {180-angles[i]}")
    end_fill()
# Settings used for entire program
tracer(0,0)
hideturtle()
width(2)
# Draw base rectangle segment
draw_tri(0, 0, 100, [30, 120, 30], "maroon", "black", centy=True)
#draw_rec(0, 0, 250, 200, "burlywood", "black", centy=True)
#draw_rec(-225, -100, 200, 125, "sienna", "black")
# Draw roof segment
# Draw chimney
# Draw door
# Draw circle window
# Draw top-center window
# Draw top-left window
# Draw top-right window
# Draw bottom-left window
# Draw bottom-right window
update()
done()
