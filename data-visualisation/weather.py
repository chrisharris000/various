#! /usr/bin/python
import os
import feedparser
import xml.etree.ElementTree as ET
import urllib

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
                max_temp = day.find("./element[@type='air_temperature_maximum']").text
                if day.find("./element[@type='air_temperature_minimum']") != None:
                    min_temp = day.find("./element[@type='air_temperature_minimum']").text
                else:
                    min_temp = max_temp
                precis = day.find("./text[@type='precis']").text
                rain_chance = day.find("./text[@type='probability_of_precipitation']").text
                if day.find("./element[@type='precipitation_range']") != None:
                    precip_range = day.find("./element[@type='precipitation_range']").text
                else:
                    precip_range = -1
                week_summary.append([start_period, end_period, weather_num,
                                   max_temp, min_temp, precis, rain_chance, precip_range])
            
            locations[town] = week_summary
    return locations
                    
root = import_data()
locations = extract_data(root)

'''Weather symbols/meaning https://github.com/sirleech/weather_feed'''
