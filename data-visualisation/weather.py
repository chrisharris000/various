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

def extract_data(root,REGIONS):
    last_issue = root[0][3].text
    next_issue = root[0][9].text
    locations = {}
    region_summary = {}
    
    forecast = root[1]
    for child in forecast:
        if child.attrib["aac"].startswith("NSW_PT"):
            town = child.attrib["description"]
            region = REGIONS[child.attrib["parent-aac"]]
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
            
            locations[town] = [region, week_summary]

    for t in REGIONS:
        region_summary[REGIONS[t]] = []
    
    for t in locations:
        region_summary[locations[t][0]].append([t,locations[t][1]])

    return region_summary

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
    window.geometry('600x600')
    return window

def create_region_dropdown(window, REGIONS):
    regions = sorted(REGIONS.values())
    region_dropdown = Combobox(window)
    region_dropdown.bind("<<ComboboxSelected>>", handle_region_change)
    region_dropdown["values"] = tuple(regions)
    region_dropdown.current(regions.index("Sydney Metropolitan"))
    region_dropdown.grid(row = 0, column = 0)
    return region_dropdown

def create_area_dropdown(window, region_value, region_summary):
    areas = []
    for r in region_summary:
        if r == region_value:
            for town in region_summary[r]:
                areas.append(town[0])
    areas = sorted(areas)
    
    area_dropdown = Combobox(window)
    area_dropdown.bind("<<ComboboxSelected>>", handle_area_change)
    area_dropdown["values"] = tuple(areas)
    area_dropdown.current(areas.index("Parramatta"))
    area_dropdown.grid(row = 0, column = 1)
    return area_dropdown

def handle_region_change(event):
    region_var.set(region_dropdown.get())

def handle_area_change(event):
    area_var.set(area_dropdown.get())

REGIONS = {"NSW_PW005":"Sydney Metropolitan",
               "NSW_PW017":"Australian Capital Territory",
               "NSW_PW001":"Northern Rivers",
               "NSW_PW002":"Mid North Coast",
               "NSW_PW003":"Hunter",
               "NSW_PW004":"Northern Tablelands",
               "NSW_PW006":"Illawarra",
               "NSW_PW007":"South Coast",
               "NSW_PW008":"Central Tablelands",
               "NSW_PW009":"Southern Tablelands",
               "NSW_PW011":"North West Slopes and Plains",
               "NSW_PW012":"Central West Slopes and Plains",
               "NSW_PW013":"South West Slopes",
               "NSW_PW014":"Riverina",
               "NSW_PW015":"Lower Western",
               "NSW_PW016":"Upper Western",
               "NSW_PW010":"Snowy Mountains"}

root = import_data()
region_summary = extract_data(root,REGIONS)

window = create_window()
region_dropdown = create_region_dropdown(window, REGIONS)
area_dropdown = create_area_dropdown(window, "Sydney Metropolitan", region_summary)

region_var = StringVar()
region_var.set("Sydney Metropolitan")
region_lbl = Label(window,textvariable=region_var).grid(row = 0, column = 2)
area_var = StringVar()
area_var.set("Parramatta")
area_lbl = Label(window,textvariable=area_var).grid(row = 0, column = 3)

window.mainloop()

#root = import_data()
#locations = extract_data(root)
'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
