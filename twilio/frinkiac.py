import schedule
import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

'''
Adapted from https://www.pluralsight.com/guides/build-a-simpsons-quote-bot-with-twilio-mms-frinkiac-and-python
'''
account_sid = ''
auth_token  = ''

client = Client(account_sid, auth_token)


def get_quote():
    r = requests.get("https://frinkiac.com/api/random")
    if r.status_code == 200:
        json = r.json()

        # Combine each line of subtitles into one string.
        caption = "\n".join([subtitle["Content"] for subtitle in json["Subtitles"]])
        caption += "\n" + json['Episode']['Key'] +  ' - ' + json['Episode']['Title']
        return caption

def send_MMS():
    body = get_quote()
    try:
        message = client.messages.create(
            body=body,
            to="",
            from_="")
        
        print("Message sent!")
    # If an error occurs, print it out.
    except TwilioRestException as e:
        print(e)

schedule.every().day.at("08:00").do(send_MMS)

while True:
    schedule.run_pending()
