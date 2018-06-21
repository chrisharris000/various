#! /usr/bin/python
import os
import feedparser
import urllib

def import_data():
    data = urllib.request.urlopen("ftp://ftp2.bom.gov.au/anon/gen/fwo/IDN10064.txt") #sydney's forcast
    info = []
    for line in data:
        line = line.decode("utf-8").replace("\n","")
        info.append(line)
    return info

def prettify_data(info):
    last_issue = ""
    text_today = ""
    city_sum = []
    penrith_sum = []
    syd_sum = []
    
    for line in info:
        if line == "Sydney Forecast":
            time_i = info.index(line)
            last_issue = info[time_i+1]

        if line.startswith("Forecast for the rest of"):
            text_i = info.index(line)
            text_today = info[text_i+1]

        if line.startswith("City Centre"):
            rain_chance_i = info.index(line) + 1
            summary = ' '.join(line.split())
            rain_chance = info[rain_chance_i].strip()
            city_sum.append([summary,rain_chance])

        if line.startswith("Penrith"):
            rain_chance_i = info.index(line) + 1
            summary = ' '.join(line.split())
            rain_chance = info[rain_chance_i].strip()
            penrith_sum.append([summary,rain_chance])

        if line == "Around Sydney":
            next_i = info.index(line) + 1
            for i in range(3):
                s = info[next_i].split()
                if s[0] == "Liverpool":
                    location = s[3] + " " + s[4]
                    syd_sum.append([s[0],s[2]])
                    syd_sum.append([location,s[6]])
                else:
                    syd_sum.append([s[0],s[2]])
                    syd_sum.append([s[3],s[5]])
                next_i += 1
            
    return last_issue, text_today, city_sum, penrith_sum, syd_sum
                    
info = import_data()
p = prettify_data(info)
print("Last issue")
print(p[0])
print("Text today")
print(p[1])
print("City Summary")
print(p[2])
print("Penrith Summary")
print(p[3])
print("Sydney Summary")
print(p[4])
