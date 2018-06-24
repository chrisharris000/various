from tkinter import *
import weather_format

#use one trace on area to produce entire week output

def update_options(*args):
        region = region_town_summary[region_var.get()]
        area_var.set(region[0])

        menu = area_optionmenu['menu']
        menu.delete(0, 'end')

        for area in region:
            menu.add_command(label=area, command=lambda locality=area: area_var.set(locality))

def update_summary(*args):
        current_weather = get_current_weather(region_weather_summary, region_var, area_var)
        start_var.set(current_weather[0])
        end_var.set(current_weather[1])
        precis_var.set(current_weather[5])

def update_week_weather(*args):
        week_summary = get_week_weather(region_weather_summary, region_var, area_var)[0]
        for v in var_list:
                data = week_summary[var_list.index(v)]
                v.set(data)

def create_window():
    window = Tk()
    window.title("Weather Forecast")
    window.geometry('600x600')
    return window

def get_current_weather(region_weather_summary, region_var, area_var):
        region_weather = region_weather_summary[region_var.get()]
        for suburb in region_weather:
                if suburb[0] == area_var.get():
                        weather_today = suburb[1][0]
        return weather_today

def get_week_weather(region_weather_summary, region_var, area_var):       
        region_weather = region_weather_summary[region_var.get()]
        for suburb in region_weather:
                if suburb[0] == area_var.get():
                        week_weather = suburb[1][1:]
        return week_weather

def create_widgets(window, day_summary):
        lbl_list = []
        var_list = []
        for data in day_summary:
                temp_var = StringVar()
                temp_var.set(data)
                lbl = Label(window, textvariable = temp_var)
                lbl.grid(row = 12 + day_summary.index(data), column = 0)
                lbl_list.append(lbl)
                var_list.append(temp_var)
        return lbl_list,var_list

root = weather_format.import_data()
REGIONS = weather_format.region_codes()
region_weather_summary, region_town_summary = weather_format.extract_data(root, REGIONS)


window = create_window()

#create StringVar() objects
region_var = StringVar()
area_var = StringVar()
start_var = StringVar()
end_var = StringVar()
precis_var = StringVar()

#create trace for StringVar() 's that need to be updated when dropdow selection changes
region_var.trace('w', update_options)
area_var.trace('w',update_summary)

#create fropdown menus
region_optionmenu = OptionMenu(window, region_var, *sorted((region_town_summary.keys())))
area_optionmenu = OptionMenu(window, area_var, '')

#initialise StringVar() 's
region_var.set('Sydney Metropolitan')
area_var.set("Parramatta")
current_weather = get_current_weather(region_weather_summary, region_var, area_var)
start_var.set(current_weather[0])
end_var.set(current_weather[1])
precis_var.set(current_weather[5])

#initialise Labels with values
title_lbl = Label(window, text = "Weather Forecast")
region_lbl = Label(window, textvariable = region_var)
area_lbl = Label(window, textvariable = area_var)

curr_weather_lbl = Label(window,text = "Summary of Weather Today")
start_lbl = Label(window, textvariable = start_var)
end_lbl = Label(window, textvariable = end_var)
precis_lbl = Label(window, textvariable = precis_var)

#tomorrow Label creation
week_summary = get_week_weather(region_weather_summary, region_var, area_var)
lbl_list,var_list = create_widgets(window, week_summary[0])

#place widgets in window
title_lbl.grid(row = 0, column = 3)
region_optionmenu.grid(row = 1, column = 0)
region_lbl.grid(row = 1, column = 3)
area_optionmenu.grid(row = 1, column = 1)
area_lbl.grid(row = 1, column = 4)

curr_weather_lbl.grid(row = 2, column = 3)
start_lbl.grid(row = 3, column = 0)
end_lbl.grid(row = 4, column = 0)
precis_lbl.grid(row = 5, column = 0)

window.mainloop()

'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
