#!/usr/bin/python
from tkinter import *
from tkinter import ttk
import webbrowser
import news_format
 
def create_window():
    window = Tk()
    window.title('News Feed')
    window.geometry('1000x500')
    return window

def create_notebook(window):
    nb = ttk.Notebook(window)
    return nb

def weight_cells(window):
    rows = 0
    while rows < 100:
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
    lbl = Label(tab, text = text, wraplength = 750, justify = LEFT)
    lbl.grid(row = row, column = column)

def create_button(tab, row, column, text, command):
    btn = Button(tab, text = text, command = command)
    btn.grid(row = row, column = column)

def open_link():
    webbrowser.open(link)

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
        if stories.index(article) <= 5:
            title = article['title']
            article_summary = article['article_summary']
            link = article['link']
            create_label(tab, r, c, title)
            create_label(tab, r + 1, c, article_summary)
            r += 2

nb.grid(row=1, column=0, columnspan=500, rowspan=500, sticky='NESW')    


window.mainloop()
