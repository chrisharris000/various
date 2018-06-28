from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import weather_format

def update_options(*args):
    region = region_town_summary[region_var.get()]
    area_var.set(region[0])
    menu = area_optionmenu['menu']
    menu.delete(0, 'end')
    for area in region:
        menu.add_command(label=area, command=lambda locality=area: area_var.set(locality))

def update_summary(*args):
    week_weather = get_week_weather(region_weather_summary, region_var, area_var)
    r = 10
    c = 0
    for day in week_weather:
        for value in day:
            delete_label(r, c)
            if c == 2:
                file = weather_format.code_to_file(int(value))
                image = Image.open(file)
                photo = ImageTk.PhotoImage(image)
                icon_lbl = Label(image = photo)
                icon_lbl.image = photo
                icon_lbl.grid(row = r, column = c)
            
            else:
                if day.index(value) == 0 or day.index(value) == 1:
                    value = weather_format.format_time(value)
                    value = weather_format.get_day(value[0]) + " " + value[0] + " " + value[1]
                create_label(value,r,c)
                
            c += 1
        c = 0
        r += 1

def update_week_weather(*args):
    week_summary = get_week_weather(region_weather_summary, region_var, area_var)[0]
    for v in var_list:
        data = week_summary[var_list.index(v)]
        v.set(data)

def create_window():
    window = Tk()
    window.title("Weather Forecast")
    return window

def get_week_weather(region_weather_summary, region_var, area_var):
    region_weather = region_weather_summary[region_var.get()]
    for suburb in region_weather:
        if suburb[0] == area_var.get():
            week_weather = suburb[1]
    return week_weather

def create_label(text, row, column, pad = False):
    var = StringVar()
    var.set(text)
    lbl = Label(window,textvariable = var)
    if pad == True:
        lbl.grid(row = row, column = column, padx = 10)
    else:
        lbl.grid(row = row, column = column)
    return lbl

def delete_label(row, column):
    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) == row and int(label.grid_info()["column"]) == column:
            label.grid_forget()

def open_data():
    webbrowser.open("ftp://ftp.bom.gov.au/anon/gen/fwo/IDN11060.xml")

def open_github():
    webbrowser.open("https://github.com/chrisharris000/various/tree/master/weather")

root = weather_format.import_data()
REGIONS = weather_format.region_codes()
region_weather_summary, region_town_summary = weather_format.extract_data(root, REGIONS)


window = create_window()

#create StringVar() objects
region_var = StringVar()
area_var = StringVar()

#create trace for StringVar() 's that need to be updated when dropdow selection changes
region_var.trace('w', update_options)
area_var.trace('w',update_summary)

#create dropdown menus
region_optionmenu = OptionMenu(window, region_var, *sorted((region_town_summary.keys())))
area_optionmenu = OptionMenu(window, area_var, '')

#create buttons
data_btn = Button(window, text = "BOM Data Source", command=open_data)
github_btn = Button(window, text = "GitHub", command=open_github)

#initialise StringVar() 's
region_var.set('Sydney Metropolitan')
area_var.set("Parramatta")

#initialise Labels with values
title_lbl = Label(window, text = "Weather Forecast")

headings = ["Start of Period", "End of Period", "", "Min Temp °C", "Max Temp °C",
            "Description", "Probability of Precipitation", "Precipitation Range"]
heading_lbls = []
for c in range(8):
    lbl = create_label(headings[c] + '\n', 4, c, pad = True)
    heading_lbls.append(lbl)
    
curr_weather_lbl = Label(window,text = "Summary of Weather for the Week\n")
data_lbl = Label(window, text = "\nWeather Data: ftp://ftp.bom.gov.au/anon/gen/fwo/IDN11060.xml\n\nCreated by Chris - https://github.com/chrisharris000")

#style labels
title_lbl.config(font=(None, 20, "bold"))
curr_weather_lbl.config(font=(None,15,"bold"))
for l in heading_lbls:
    l.config(font=(None,12,"bold"))

#place widgets in window
title_lbl.grid(row = 0, column = 0)
region_optionmenu.grid(row = 1, column = 0)
area_optionmenu.grid(row = 2, column = 0)
curr_weather_lbl.grid(row = 3, column = 3, columnspan = 2)
data_lbl.grid(row = 20, column = 0)
data_btn.grid(row = 21, column = 0)
github_btn.grid(row = 21, column = 1)

window.iconbitmap('sunny_icon.ico')
window.mainloop()
