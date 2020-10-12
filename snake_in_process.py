from tkinter import Tk, Canvas

# Globals
width = 500
height = 500
seg_size = 10

# Setting up window
root = Tk()
root.title("Python Snake")
c = Canvas(root, width=width, height=height, bg="#000000")
c.grid()

# From OOP


def create_text(x, y, text, color='white'):
    return c.create_text(x, y, text=text, font='Arial 20', fill=color)


create_text(200, 400, '*')
create_text(100, 200, '#')

# Start window
root.mainloop()

