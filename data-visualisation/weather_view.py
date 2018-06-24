from tkinter import *

def update_options(*args):
        
        region = region_town_summary[region_var.get()]
        area_var.set(region[0])

        menu = area_optionmenu['menu']
        menu.delete(0, 'end')

        for area in region:
            menu.add_command(label=area, command=lambda locality=area: area_var.set(locality))

region_town_summary = {'Snowy Mountains': ['Jindabyne', 'Bombala', 'Charlotte Pass', 'Cooma', 'Thredbo Top Station', 'Perisher Valley', 'Selwyn', 'Cabramurra'], 'Hunter': ['The Entrance', 'Cessnock', 'Gosford', 'Scone', 'Muswellbrook', 'Wallsend', 'Wyong', 'Toronto', 'Raymond Terrace', 'Maitland', 'Woy Woy', 'Singleton', 'Nelson Bay', 'Newcastle'], 'Central Tablelands': ['Springwood', 'Wellington', 'Katoomba', 'Orange', 'Bathurst', 'Jenolan Caves', 'Mudgee', 'Lithgow'], 'Upper Western': ['Bourke', 'Wilcannia', 'Tibooburra', 'Cobar', 'Brewarrina'], 'Illawarra': ['Port Kembla', 'Albion Park', 'Wollongong', 'Bulli', 'Huskisson', 'Bowral', 'Kiama', 'Nowra'], 'Riverina': ['Albury', 'Deniliquin', 'Junee', 'Finley', 'Griffith', 'Narrandera', 'Wagga Wagga', 'Hay', 'Corowa'], 'Lower Western': ['Menindee', 'Broken Hill', 'Ivanhoe', 'Wentworth', 'Balranald', 'Lake Mungo'], 'South Coast': ['Batemans Bay', 'Ulladulla', 'Eden', 'Bega', 'Monolith Valley', 'Narooma', 'Merimbula'], 'Northern Rivers': ['Byron Bay', 'Murwillumbah', 'Evans Head', 'Lismore', 'Ballina', 'Yamba', 'Tweed Heads', 'Grafton'], 'Central West Slopes and Plains': ['Coonamble', 'Parkes', 'West Wyalong', 'Lake Cargelligo', 'Dubbo', 'Condobolin', 'Cowra', 'Coonabarabran', 'Narromine', 'Temora', 'Nyngan', 'Forbes'], 'Australian Capital Territory': ['Belconnen', 'Canberra', 'Woden Valley', 'Mount Ginini', 'Gungahlin', 'Tuggeranong'], 'North West Slopes and Plains': ['Barraba', 'Warialda', 'Moree', 'Narrabri', 'Tamworth', 'Gunnedah', 'Walgett', 'Wee Waa', 'Quirindi'], 'South West Slopes': ['Gundagai', 'Cootamundra', 'Tumut', 'Young', 'Tumbarumba'], 'Mid North Coast': ['Taree', 'Port Macquarie', 'Wauchope', 'Barrington Tops', 'Nambucca Heads', 'Bulahdelah', 'Coffs Harbour', 'Forster', 'Kempsey', 'Dorrigo'], 'Southern Tablelands': ['Queanbeyan', 'Crookwell', 'Goulburn', 'Braidwood', 'Yass'], 'Northern Tablelands': ['Guyra', 'Glen Innes', 'Walcha', 'Armidale', 'Inverell', 'Tenterfield'], 'Sydney Metropolitan': ['Sydney Olympic Park', 'Blacktown', 'Richmond', 'Mascot', 'Canterbury', 'Terrey Hills', 'Hornsby', 'Cronulla', 'Sydney', 'Parramatta', 'Camden', 'Campbelltown', 'Mona Vale', 'Bondi', 'Liverpool', 'Penrith']}

def create_window():
    window = Tk()
    window.title("Weather Forecast")
    window.geometry('600x600')
    return window

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
