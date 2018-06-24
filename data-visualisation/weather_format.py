#! /usr/bin/python
import feedparser
import xml.etree.ElementTree as ET
import urllib
from tkinter import *
from tkinter.ttk import *

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
    region_town_summary = {}
    
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
        region_town_summary[REGIONS[t]] = []
    
    for t in locations:
        region_summary[locations[t][0]].append([t,locations[t][1]])
        region_town_summary[locations[t][0]].append(t)
    
    return region_summary, region_town_summary

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

def update_options(*args):
        
        region = region_town_summary[region_var.get()]
        area_var.set(region[0])

        menu = area_optionmenu['menu']
        menu.delete(0, 'end')

        for area in region:
            menu.add_command(label=area, command=lambda locality=area: area_var.set(locality))

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

#root = import_data()
#region_weather_summary, region_town_summary = extract_data(root,REGIONS)

region_town_summary = {'Snowy Mountains': ['Jindabyne', 'Bombala', 'Charlotte Pass', 'Cooma', 'Thredbo Top Station', 'Perisher Valley', 'Selwyn', 'Cabramurra'], 'Hunter': ['The Entrance', 'Cessnock', 'Gosford', 'Scone', 'Muswellbrook', 'Wallsend', 'Wyong', 'Toronto', 'Raymond Terrace', 'Maitland', 'Woy Woy', 'Singleton', 'Nelson Bay', 'Newcastle'], 'Central Tablelands': ['Springwood', 'Wellington', 'Katoomba', 'Orange', 'Bathurst', 'Jenolan Caves', 'Mudgee', 'Lithgow'], 'Upper Western': ['Bourke', 'Wilcannia', 'Tibooburra', 'Cobar', 'Brewarrina'], 'Illawarra': ['Port Kembla', 'Albion Park', 'Wollongong', 'Bulli', 'Huskisson', 'Bowral', 'Kiama', 'Nowra'], 'Riverina': ['Albury', 'Deniliquin', 'Junee', 'Finley', 'Griffith', 'Narrandera', 'Wagga Wagga', 'Hay', 'Corowa'], 'Lower Western': ['Menindee', 'Broken Hill', 'Ivanhoe', 'Wentworth', 'Balranald', 'Lake Mungo'], 'South Coast': ['Batemans Bay', 'Ulladulla', 'Eden', 'Bega', 'Monolith Valley', 'Narooma', 'Merimbula'], 'Northern Rivers': ['Byron Bay', 'Murwillumbah', 'Evans Head', 'Lismore', 'Ballina', 'Yamba', 'Tweed Heads', 'Grafton'], 'Central West Slopes and Plains': ['Coonamble', 'Parkes', 'West Wyalong', 'Lake Cargelligo', 'Dubbo', 'Condobolin', 'Cowra', 'Coonabarabran', 'Narromine', 'Temora', 'Nyngan', 'Forbes'], 'Australian Capital Territory': ['Belconnen', 'Canberra', 'Woden Valley', 'Mount Ginini', 'Gungahlin', 'Tuggeranong'], 'North West Slopes and Plains': ['Barraba', 'Warialda', 'Moree', 'Narrabri', 'Tamworth', 'Gunnedah', 'Walgett', 'Wee Waa', 'Quirindi'], 'South West Slopes': ['Gundagai', 'Cootamundra', 'Tumut', 'Young', 'Tumbarumba'], 'Mid North Coast': ['Taree', 'Port Macquarie', 'Wauchope', 'Barrington Tops', 'Nambucca Heads', 'Bulahdelah', 'Coffs Harbour', 'Forster', 'Kempsey', 'Dorrigo'], 'Southern Tablelands': ['Queanbeyan', 'Crookwell', 'Goulburn', 'Braidwood', 'Yass'], 'Northern Tablelands': ['Guyra', 'Glen Innes', 'Walcha', 'Armidale', 'Inverell', 'Tenterfield'], 'Sydney Metropolitan': ['Sydney Olympic Park', 'Blacktown', 'Richmond', 'Mascot', 'Canterbury', 'Terrey Hills', 'Hornsby', 'Cronulla', 'Sydney', 'Parramatta', 'Camden', 'Campbelltown', 'Mona Vale', 'Bondi', 'Liverpool', 'Penrith']}

window = create_window()

region_var = StringVar()
area_var = StringVar()

region_var.trace('w', update_options)

region_optionmenu = OptionMenu(window, region_var, *(region_town_summary.keys()))
area_optionmenu = OptionMenu(window, area_var, '')

region_var.set('Snowy Mountains')
region_optionmenu.grid(row = 0, column = 0)
area_optionmenu.grid(row = 0, column = 1)
   
window.mainloop()

'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
