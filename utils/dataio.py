import requests
import json
import pkgutil

def get_data(day, year = 2018):
    url = get_url(day, year)
    config_data = pkgutil.get_data(__package__, 'config.json')
    config = json.loads(config_data)
    r = requests.get(url, cookies=config["cookie"])
    return r.text

def get_url(day, year = 2018):
    
    return '/'.join([
        'https://adventofcode.com', str(year), 'day', str(day), 'input'
        ])