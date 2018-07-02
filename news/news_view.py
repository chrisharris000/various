#!/usr/bin/python
from tkinter import *
from tkinter import ttk
import webbrowser
import news_format
 
def create_window():
    window = Tk()
    window.title('News Feed')
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
    lbl = Label(tab, text = text, wraplength = 1000, justify = CENTER)
    lbl.grid(row = row, column = column)
    return lbl

def create_button(tab, row, column, text):
    btn = Button(tab, text = text)
    btn.grid(row = row, column = column)
    return btn

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

news_stories = news_format.information()

window = create_window()
weight_cells(window)
nb = create_notebook(window)
tabs = add_tabs(nb, list(news_stories.keys()) + ["Links"])
links = []

for index, cat in enumerate(news_stories):
    tab = tabs[index]
    stories = news_stories[cat]
    r, c = 0, 0
    for article in stories:
        if stories.index(article) <= 5:
            title = article['title']
            article_summary = article['article_summary']
            link = article['link']
            links.append(link)
            
            lbl = create_label(tab, r, c, title)
            lbl.config(font=(None, 14, 'bold'))
            
            create_label(tab, r + 1, c, article_summary + '\n\n')
            
            r += 2

r, c = 0, 0

for link in links:
    lbl = Label(tabs[-1], text = link, fg = "blue", cursor="hand2", wraplength = 1000, justify = LEFT)
    lbl.grid(row = r, column = c)
    lbl.bind("<Button-1>", callback)
    lbl.config(font=(None, 8))
    r += 1

nb.grid(row=1, column=0, columnspan=750, rowspan=750, sticky='NESW')    

window.mainloop()
