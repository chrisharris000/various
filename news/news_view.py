#!/usr/bin/python
from tkinter import *
from tkinter import ttk
 
def create_window():
    window = Tk()
    window.title('News Feed')
    window.geometry('500x500')
    return window

def create_notebook(window):
    nb = ttk.Notebook(window)
    return nb

def weight_cells(window):
    rows = 0
    while rows < 50:
        window.rowconfigure(rows, weight=1)
        window.columnconfigure(rows, weight=1)
        rows += 1

def add_tabs(nb, titles):
    tabs = []
    for name in titles:
        page = ttk.Frame(nb)
        nb.add(page, text = name)
        tabs.append(page)
    return tabs

window = create_window()
weight_cells(window)
nb = create_notebook(window)
tabs = add_tabs(nb, ["Science", "Technology"])

#cteate widgets
mybutton = Button(tabs[0], text='MyButton')
lbl = Label(tabs[1],text="Hello")

#place widgets on tabs
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
mybutton.grid(row=1,column=1)
lbl.grid(row = 3, column = 3)

window.mainloop()
