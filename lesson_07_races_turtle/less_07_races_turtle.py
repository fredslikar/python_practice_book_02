"""Fun turtle racing."""

import random
import turtle

"""Creates a list for future turtles, 
set the coordinates of the finish line"""

turtles = []
FINISH = 535


def setup():
    """Sets the coordinates of the start line,
    setup screen, its background;
    creates 5 turtles and places them on the starting line."""

    global turtles
    startline = -570
    screen = turtle.Screen()
    screen.setup(1366, 768)
    screen.bgpic('Start.gif')

    turtle_ycor = [225, 125, 25, -70, -175]
    turtle_color = ['red', 'orange', 'grey', 'blue', 'green']

    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        turtles.append(new_turtle)


def show_winner(color):
    """Prints the color winner."""

    text_pen = turtle.Turtle()
    text_pen.hideturtle()
    text_pen.penup()
    text_pen.color('white')
    text_pen.setpos(-250, 100)
    text_pen.write('Winner is ' + color + ' turtle!!!', font=("Arial", 40, "normal"))


def race():
    """Moves the turtle to the finish line, determines the winning turtle,
    its color and displays information about it."""

    global turtles
    winner = False

    while not winner:
        for curent_turtle in turtles:
            move = random.randint(0, 10)
            curent_turtle.forward(move)
            xcor = curent_turtle.xcor()
            if xcor >= FINISH:
                winner = True
                color_winner = curent_turtle.color()
                color_winner = color_winner[0]
                print('Winner is ', color_winner, ' turtle!!!')
                show_winner(color_winner)


setup()
race()
turtle.mainloop()
