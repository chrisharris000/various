#!/usr/bin/python
from tkinter import *
from tkinter import ttk
import news_format
 
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

def create_label(tab, row, column, text):
    lbl = Label(tab, text = text)
    lbl.grid(row = row, column = column)

def create_button(tab, row, column, text, command):
    btn = Button(tab, text = text, command = command)
    btn.grid(row = row, column = column)

def open_link():
    pass

news_stories = news_format.information()

window = create_window()
weight_cells(window)
nb = create_notebook(window)
tabs = add_tabs(nb, news_stories.keys())

for index, cat in enumerate(news_stories):
    tab = tabs[index]
    stories = news_stories[cat]
    r, c = 0, 0
    for article in stories:
        title = article['title']
        article_summary = article['article_summary']
        link = article['link']
        if len(article_summary) < 50:
            create_label(tab, r, c, text = title)
            create_label(tab, r + 1, c, text = article_summary)
            create_label(tab, r + 2, c, text = link)
            r += 3

nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')    
'''example
#cteate widgets
mybutton = Button(tabs[0], text='MyButton')
lbl = Label(tabs[1],text="Hello")
lbl2 = Label(tabs[1],text = "World")

#place widgets on tabs
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
mybutton.grid(row=1,column=1)
lbl.grid(row = 3, column = 3)
lbl2.grid(row = 3, column = 10)'''

window.mainloop()
