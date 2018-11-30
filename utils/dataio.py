import requests
import json
import os
import pkgutil

def get_data(day, year = 2018):
    url = get_url(day, year)
    __config_location__ = os.path.join(os.path.dirname(__file__),"config.json")
    with open(__config_location__,"r") as read_file:
        config = json.load(read_file)
    r = requests.get(url, cookies=config["cookie"])
    return r.text

def get_url(day, year = 2018):
    
    return '/'.join([
        'https://adventofcode.com', str(year), 'day', str(day), 'input'
        ])