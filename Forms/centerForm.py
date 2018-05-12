from tkinter import *
from tkinter import ttk

def centerForm(w,h, title):
    new_root = Tk()
    #Se define el nombre de la ventana y se restringe el tamaño de la misma
    new_root.title(title)
    new_root.resizable(0,0)
    new_root.geometry("{0}x{1}".format(w,h))

    # get screen width and height
    ws = new_root.winfo_screenwidth() # width of the screen
    hs = new_root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    new_root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    return new_root
