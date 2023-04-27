"""Runs the game of life
(the game based on the programming principle of cellular automata).
Uses logic and functions from file 'life_model.py', tkinter window."""

from tkinter import Tk, Canvas, Button, StringVar, OptionMenu, W, E, ALL, mainloop
import life_model

x = life_model.x
y = life_model.y
cell_size = 5
is_running = False


def setup_window():
    """Creates instance of the class Tk with menu and buttons.
    The main window with the playing field."""

    global root
    global matrix_view
    global cell_size
    global start_button
    global clear_button
    global choice

    root = Tk()
    root.title('The game of life')

    # Game field
    matrix_view = Canvas(root,
                         width=life_model.x * cell_size,
                         height=life_model.y * cell_size,
                         borderwidth=0,
                         bg='white'
                         )

    # Buttons setup
    start_button = Button(root, text='Start', width=12)
    start_button.bind('<Button-1>', start_handler)
    clear_button = Button(root, text='Clear', width=12)
    clear_button.bind('<Button-1>', clear_handler)

    # Drop down menu setup
    choice = StringVar(root)
    choice.set('Choice pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random', command=option_handler)
    option.config(width=20)

    # Arrangement of window elements
    matrix_view.grid(row=0, columnspan=3, padx=20, pady=20)
    matrix_view.bind('<Button-1>', matrix_handler)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


def option_handler(event):
    """Selection options for the drop-down menu."""

    global start_button
    global is_running
    global choice

    is_running = False
    start_button.configure(text='Start')
    selection = choice.get()
    if selection == 'glider':
        life_model.load_pattern(life_model.glider_pattern, 10, 10)
    elif selection == 'glider gun':
        life_model.load_pattern(life_model.glider_gun_pattern, 10, 10)
    elif selection == 'random':
        life_model.random_matrix(life_model.matrix, life_model.x, life_model.y)


def matrix_handler(event):
    """Reproduces the logic of displaying cells:
    alive cell- black, dead cell - white"""

    global matrix_view
    global cell_size

    row = int(event.x / cell_size)
    col = int(event.y / cell_size)

    if life_model.matrix[row][col] == 1:
        life_model.matrix[row][col] = 0
        draw_cell(row, col, 'white')
    else:
        life_model.matrix[row][col] = 1
        draw_cell(row, col, 'black')


def clear_handler(event):
    """Clears game field with use clear_button."""

    global clear_button
    life_model.matrix = life_model.matrix_start(x, y)
    update()


def start_handler(event):
    """Runs game if it is stopped..."""

    global is_running
    global start_button

    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Pause')
        update()


def update():
    """Updates the playing field according to the logic:
    non-living cell - white,
    first generation cell - sky blue,
    the second - gray,
    the third - black,
    more than a third is red."""

    global matrix_view
    matrix_view.delete(ALL)
    life_model.create_new_matrix()
    for i in range(life_model.x):
        for j in range(life_model.y):
            if life_model.gen_list[i][j] == 1:
                draw_cell(i, j, 'sky blue')
            if life_model.gen_list[i][j] == 2:
                draw_cell(i, j, 'grey')
            if life_model.gen_list[i][j] == 3:
                draw_cell(i, j, 'black')
            if life_model.gen_list[i][j] > 3:
                draw_cell(i, j, 'red')

    if is_running:
        root.after(100, update)


def draw_cell(row, col, color):
    global matrix_view
    global cell_size

    if color == 'black':
        outline = 'white'
    else:
        outline = 'white'

    matrix_view.create_rectangle(row * cell_size, col * cell_size, row * cell_size + cell_size,
                                 col * cell_size + cell_size,
                                 fill=color, outline=outline)


if __name__ == '__main__':
    setup_window()
    update()
    mainloop()
