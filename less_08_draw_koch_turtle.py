"""Draw koch figure."""

import turtle


def setup(pen):
    pen.color('blue')
    pen.penup()
    pen.goto(-200, 100)
    pen.speed(0)
    pen.pendown()


def koch(pen, size, order):
    if order == 0:
        pen.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(pen, size/3, order-1)
            pen.left(angle)


def main():
    pen = turtle.Turtle()
    setup(pen)
    order = 5
    size = 400

    for i in range(3):
        koch(pen, size, order)
        pen.right(120)


if __name__ == '__main__':
    main()
    turtle.tracer(100)  # Speed of drawing
    turtle.mainloop()