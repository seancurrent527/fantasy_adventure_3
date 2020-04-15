import tkinter as tk, argparse
from random import randint

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type = int, default = 100)
    return parser.parse_args()

def create_dice(color, size):
    """
    Creates the dice with all the sides drawn in a list.
    The sides are drawn by the draw_dice function.

    :return: dice list
    """
    dice = list()
    dice.append(draw_dice(color, size, 'dot0'))  # empty
    dice.append(draw_dice(color, size, 'dot4'))  # center dot --> 1
    dice.append(draw_dice(color, size, 'dot3', 'dot5'))  # dice head 2
    dice.append(draw_dice(color, size, 'dot2', 'dot4', 'dot6'))  # dice head 3
    dice.append(draw_dice(color, size, 'dot1', 'dot2', 'dot6', 'dot9'))  # dice head 4
    dice.append(draw_dice(color, size, 'dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  # dice head 5
    dice.append(draw_dice(color, size, 'dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  # dice head 6
    return dice

def create_six_dice(size):
    dice = {}
    for color in colors:
        display_color = color if not color.startswith('white') else 'white'
        dice[color] = create_dice(display_color, size)
    return dice

def draw_dice(color, size, *args):
    """
    Creates the individual heads passed in through the 
    create_dice function.

    :param args: string(s) for certain dots for certain heads
    :return: c canvas
    """
    w, h = size, size # sets width and height
    x, y, r = 3 * size / 45, 3 * size / 45, 10 * size / 45 # sets x, y, and radius
    c = tk.Canvas(root, width=w, height=h, bg=color) # creates canvas c

    a, b = 30 * size / 45, 15 * size / 45

    #Dictionary containing lambda functions to draw dots on canvas c
    dots = {
        'dot0': lambda x, y, r: c,
        'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
        'dot2': lambda x, y, r: c.create_oval(x + a, y, (x + a) + r, y + r, fill='black'),
        'dot3': lambda x, y, r: c.create_oval(x, y + b, x + r, (y + b) + r, fill='black'),
        'dot4': lambda x, y, r: c.create_oval(x + b, (y + b), (x + b) + r, (y + b) + r, fill='black'),
        'dot5': lambda x, y, r: c.create_oval(x + a, (y + b), (x + a) + r, (y + b) + r, fill='black'),
        'dot6': lambda x, y, r: c.create_oval(x, y + a, x + r, (y + a) + r, fill='black'),
        'dot9': lambda x, y, r: c.create_oval(x + a, y + a, (x + a) + r, (y + a) + r, fill='black')
    }

    for arg in args:
        dots.get(arg)(x, y, r) # Gets the dictionary keys while passing in x, y, and r values

    return c


def click():
    """
    Performs the operation of clicking the button. This will roll through
    the different dice heads

    :return: None
    """
    for i in range(len(colors)):
        t = 10 # start with a time delay of 100 ms and increase it as the dice rolls
        stop = randint(13, 18) # chooses random number between 13 - 17
        for x in range(stop):
            dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
            color_dice[colors[i]][dice_index].grid(row=2, column=3*i, columnspan=3)
            root.update()
            if x == stop - 1:
                # set text to the selected result
                texts[i].set(str(x % 6 + 1))
                break
            root.after(t, color_dice[colors[i]][dice_index].grid_forget()) # forgets the grid and restarts
            t += 5

if __name__ == '__main__':
    args = parse_args()

    # create the window form
    root = tk.Tk()
    root.title("Dice Roll")

    colors = ['red', 'yellow', 'green', 'blue', 'white1', 'white2']

    # create the result label
    texts = []
    for i in range(len(colors)):
        # StringVar() updates result label automatically
        text = tk.StringVar()
        # set initial value of text
        text.set("  ")
        result = tk.Label(root, textvariable=text, font = ('Helvetica', args.size // 4), fg='black')
        result.grid(row=3, column=3*i, columnspan=3)
        texts.append(text)

    color_dice = create_six_dice(args.size)

    # start with an empty canvas
    for i in range(len(colors)):
        color_dice[colors[i]][0].grid(row=2, column=3*i, columnspan=3)
    
    button1 = tk.Button(root, text="Roll", command=click)
    button1.grid(row=1, column=0, padx=3, pady=3)
    button2 = tk.Button(root, text="Quit", command=root.destroy)
    button2.grid(row=1, column=17, pady=3)

    # start of program event loop
    root.mainloop()