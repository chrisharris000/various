#! /usr/bin/python
import feedparser
import xml.etree.ElementTree as ET
import urllib
from tkinter import *
from tkinter.ttk import *
import time

def import_data():
    data = urllib.request.urlopen("ftp://ftp.bom.gov.au/anon/gen/fwo/IDN11060.xml")
    tree = ET.parse(data)
    root = tree.getroot()
    return root

def extract_data(root):
    last_issue = root[0][3].text
    next_issue = root[0][9].text
    locations = {}
    
    forecast = root[1]
    for child in forecast:
        if child.attrib["aac"].startswith("NSW_PT"):
            town = child.attrib["description"]
            week_summary = []
            for day in child:
                start_period = day.attrib["start-time-local"]
                end_period = day.attrib["end-time-local"]
                weather_num = day.find("./element[@type='forecast_icon_code']").text
                
                if day.find("./element[@type='air_temperature_maximum']") != None:
                    max_temp = day.find("./element[@type='air_temperature_maximum']").text
                else:
                    max_temp = "Unavailable"
                    
                if day.find("./element[@type='air_temperature_minimum']") != None:
                    min_temp = day.find("./element[@type='air_temperature_minimum']").text
                else:
                    min_temp = "Unavailable"
                    
                precis = day.find("./text[@type='precis']").text
                rain_chance = day.find("./text[@type='probability_of_precipitation']").text
                
                if day.find("./element[@type='precipitation_range']") != None:
                    precip_range = day.find("./element[@type='precipitation_range']").text
                else:
                    precip_range = "Unavailable"
                    
                week_summary.append([start_period, end_period, weather_num,
                                   max_temp, min_temp, precis, rain_chance, precip_range])
            
            locations[town] = week_summary
    return locations

def format_time(s):
    d,t = s.split("T")
    if t.endswith("Z"):
        t = t.replace("Z","")
    else:
        t = t.split("+")[0]
    return d,t

def create_window():
    window = Tk()
    window.title("Weather Forecast")
    window.geometry('350x200')
    return window

def create_dropdown(window, locations):
    areas = []
    for l in locations:
        areas.append(l)
    areas = sorted(areas)

    dropdown = Combobox(window)
    dropdown.bind("<<ComboboxSelected>>", handle_menu)
    dropdown["values"] = tuple(areas)
    dropdown.current(areas.index("Parramatta"))
    dropdown.grid(row = 0, column = 0)
    return dropdown

def handle_menu(event):
    lbl.grid_forget()
    lbl = Label(window, text = dropdown.get())

root = import_data()
locations = extract_data(root)
window = create_window()
dropdown = create_dropdown(window, locations)
lbl = Label(window,text=dropdown.get())
lbl.grid(row = 0, column = 1)
window.mainloop()

#root = import_data()
#locations = extract_data(root)
'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
