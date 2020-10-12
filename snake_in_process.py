from tkinter import Tk, Canvas

# Globals
width = 500
height = 500
seg_size = 10

# Setting up window
root = Tk()
root.title("PythonicWay Snake")
c = Canvas(root, width=width, height=height, bg="#000000")
c.grid()

# From OOP
x1 = 100
y1 = 200
color1 = 'white'
c.create_rectangle(x1, y1, x1 + seg_size, y1 + seg_size, fill=color1)

x2 = 200
y2 = 400
color2 = 'green'
c.create_rectangle(x2, y2, x2 + seg_size, y2 + seg_size, fill=color2)


def create_rectangle(x, y, color):
    return c.create_rectangle(x, y, x + seg_size, y + seg_size, fill=color)


create_rectangle(300, 490, 'red')



# Start window
root.mainloop()
