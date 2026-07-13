import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Continuous Heart String Art")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)

colors = ["red", "deeppink", "hotpink", "tomato"]

# Generate heart points
points = []
N = 500

for i in range(N):
    a = 2 * math.pi * i / N
    x = 16 * math.sin(a) ** 3
    y = (
        13 * math.cos(a)
        - 5 * math.cos(2 * a)
        - 2 * math.cos(3 * a)
        - math.cos(4 * a)
    )
    points.append((x * 18, y * 18))

skip = 0

while True:
    t.clear()

    for i in range(N):
        t.color(colors[(i + skip) % len(colors)])

        p1 = points[i]
        p2 = points[(i + skip) % N]

        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)

    screen.update()
    skip += 1