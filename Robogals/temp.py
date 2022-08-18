import csv, requests, time
from datetime import datetime
from bs4 import BeautifulSoup
from googlesearch import search
from postcode_regions import postcode_to_region

def get_first_google_result(query):
    return list(search(query, num=1, stop=1, pause=2))[0]

def extract_public_school_address(address):
    return " ".join(address.split("address")[-1].strip().split())

def extract_public_school_phone_number(number):
    return number.split("telephone")[-1].strip()

# data source: https://en.wikipedia.org/wiki/List_of_government_schools_in_New_South_Wales

start_time = time.time()
print("Start Time:", datetime.now().strftime("%H:%M:%S"))
print()

school_name = "TEMP"

website_address = "https://shortland-p.schools.nsw.gov.au/"
page = requests.get(website_address)

soup = BeautifulSoup(page.content, 'html.parser')

try:
    school_address_raw = soup.find("div", class_="local-footer").find("p", class_="uk-width-1-2").get_text()
    school_address = extract_public_school_address(school_address_raw)
    postcode = school_address.split()[-1]
    region = postcode_to_region(int(postcode))
except:
    school_address = "NULL"
    postcode = "NULL"
    region = "NULL"
    print(school_name, "Address find error")
    
try:
    phone_number_raw = soup.find("div", class_="local-footer").find("p", class_="local-footer-phone").get_text()
    phone_number = extract_public_school_phone_number(phone_number_raw)
except:
    phone_number = "NULL"
    print(school_name, "Phone number find error")
    
try:
    email = soup.find("div", class_="local-footer").find("p", class_="local-footer-email").find("a", href=True).get_text()
except:
    email = "NULL"
    print(school_name, "Email find error")
    
try:
    directions = soup.find("div", class_="local-footer").find("p", class_="local-footer-directions").find("a", href=True)["href"]
except:
    directions = "NULL"
    print(school_name, "Directions find error")
                
print(school_address + "\t" + postcode + "\t" + region + "\t" + phone_number + "\t" + email + "\t" + directions + "\t" + website_address)
end_time = time.time()

print()
print("End Time:", datetime.now().strftime("%H:%M:%S"))
print("Total time:", (end_time - start_time)/60)

