"""For fun - crazy turtles."""

import turtle
import random

slowpok = turtle.Turtle()
slowpok.shape('turtle')
slowpok.color('blue')

poky = turtle.Turtle()
poky.shape('turtle')
poky.color('red')

strage = turtle.Turtle()
strage.color('green')
strage.shape('turtle')


def make_squer(a_turle):
    for i in range(4):
        a_turle.forward(100)
        a_turle.right(90)

def make_squer_koch(a_turle, size, order):
    if order == 0:
        for i in range(4):
            a_turle.forward(size)
            a_turle.right(90)
    else:
        for i in range(4):
            make_squer_koch(a_turle, size/2, order-1)


def make_spiral(a_turtle, numbers=36, angle=9, forw=10):
    for i in range(numbers):
        make_squer(a_turtle)
        a_turtle.right(angle)
        a_turtle.forward(forw)


def meny_seides(a_turtle, sides=4, len_side=250):
    angles = 360/sides
    for i in range(sides):
        a_turtle.forward(len_side)
        a_turtle.right(angles)


def star(a_turtle, num_angles = 5, len=100):
    if num_angles % 2 == 1:
        for i in range(num_angles):
            a_turtle.forward(len)
            a_turtle.right(360/(2*num_angles/(num_angles + 1)))
    else:
        meny_seides(a_turtle,num_angles, len)


def crazy(a_turtle,  b_turtle, c_turtle):
    while True:
        a_turtle.forward(random.randint(35, 50))
        a_turtle.right(random.randint(0, 360))
        if -500 >= a_turtle.xcor() or a_turtle.xcor() >= 500:
            a_turtle.goto(0, 0)
        if -300 >= a_turtle.ycor() or a_turtle.ycor() >= 300:
            a_turtle.goto(0, 0)
        b_turtle.forward(random.randint(0, 100))
        b_turtle.right(random.randint(0, 360))
        if -500 >= b_turtle.xcor() or b_turtle.xcor() >= 500:
            b_turtle.goto(0, 0)
        if -300 >= b_turtle.ycor() or b_turtle.ycor() >= 300:
           b_turtle.goto(0, 0)
        c_turtle.forward(random.randint(0, 300))
        c_turtle.right(random.randint(0, 360))
        print(c_turtle.ycor())
        if -500 >= c_turtle.xcor() or c_turtle.xcor() >= 500:
            c_turtle.goto(0, 0)
        if -300 >= c_turtle.ycor() or c_turtle.ycor() >= 300:
           c_turtle.goto(0, 0)



def crazy2():
    l_turtles = {0 : slowpok, 1 : poky, 2 : strage}
    x = 0
    while True:
        for i in range(len(l_turtles)):
            l_turtles[i].forward(random.randint(-250, 250))
            l_turtles[i].right(random.randint(0, 720))
            l_turtles[i].speed(0)
            if -500 >= l_turtles[i].xcor() or l_turtles[i].xcor() >= 500:
                l_turtles[i].goto(random.randint(-500, 500), random.randint(-300, 300))
            if -300 >= l_turtles[i].ycor() or l_turtles[i].ycor() >= 300:
                l_turtles[i].goto(random.randint(-500, 500), random.randint(-300, 300))
            x += 1
            print(x)
            if x % 15 == 0:
                tur = turtle.Turtle()
                tur.shape('turtle')
                color = ['blue', 'red', 'white', 'yellow', 'grey', 'black', 'green', 'orange', 'skyblue', 'violet']
                tur.color(color[random.randint(0, 9)])
                l_turtles[i+1] = tur




crazy2()


turtle.mainloop()