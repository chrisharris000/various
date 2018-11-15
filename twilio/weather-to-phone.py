#! /usr/bin/python
import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen
from urllib.error import URLError
import datetime
import sys
import schedule
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid = ''
auth_token  = ''

client = Client(account_sid, auth_token)

def get_weather():
    caption = ''
    url = "ftp://ftp.bom.gov.au/anon/gen/fwo/IDN11060.xml"
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError as e:
        print("Failed to reach the server.")
        print("Reason:",e.reason)
        sys.exit()
    else:   
        tree = ET.parse(response)
        root = tree.getroot()

    forecast = root[1]
    for location in forecast:
        if location.attrib['aac'].startswith('NSW_PT'):
            town = location.attrib['description']

            if town == 'Parramatta':
                today = location[0]
                rain_chance = today.find("./text[@type='probability_of_precipitation']").text
                if rain_chance != None and int(rain_chance[:-1]) > 50:
                    return "Umbrella Required"

            if town == 'Mascot':
                today = location[0]
                rain_chance = today.find("./text[@type='probability_of_precipitation']").text
                if rain_chance != None and int(rain_chance[:-1]) > 50:
                    return "Umbrella Required"
                    
    return "Umbrella NOT Required"

def send_MMS():
    body = get_weather()
    try:
        message = client.messages.create(
            body=body,
            to="",
            from_="")
        
        print("Message sent!")
    # If an error occurs, print it out.
    except TwilioRestException as e:
        print(e)

schedule.every().day.at("06:30").do(send_MMS)

while True:
    schedule.run_pending()
