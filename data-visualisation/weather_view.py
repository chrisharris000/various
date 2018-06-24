from tkinter import *
import weather_format

def update_options(*args):
        
        region = region_town_summary[region_var.get()]
        area_var.set(region[0])

        menu = area_optionmenu['menu']
        menu.delete(0, 'end')

        for area in region:
            menu.add_command(label=area, command=lambda locality=area: area_var.set(locality))


def create_window():
    window = Tk()
    window.title("Weather Forecast")
    window.geometry('600x600')
    return window

root = weather_format.import_data()
REGIONS = weather_format.region_codes()
region_weather_summary, region_town_summary = weather_format.extract_data(root, REGIONS)

window = create_window()

region_var = StringVar()
area_var = StringVar()

region_var.trace('w', update_options)

region_optionmenu = OptionMenu(window, region_var, *sorted((region_town_summary.keys())))
area_optionmenu = OptionMenu(window, area_var, '')

region_var.set('Sydney Metropolitan')
area_var.set("Parramatta")
region_optionmenu.grid(row = 0, column = 0)
area_optionmenu.grid(row = 0, column = 1)
   
window.mainloop()

'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
