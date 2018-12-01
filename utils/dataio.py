import requests
import json
import pkgutil
import os
import re

def load_data(day, year = 2018):
    filename = ''.join(['data//', str(year), '//day', str(day), '.dat'])
    if not os.path.exists(filename):
        data = get_data(day, year)
        with open( filename , 'wt') as file:
            file.write(data)
    else:
        with open( filename , 'r') as file:
            data = file.read()
    return data

def get_data(day, year = 2018):
    url = get_url(day, year)
    config_data = pkgutil.get_data(__package__, 'config.json')
    config = json.loads(config_data)
    r = requests.get(url, cookies=config["cookie"])
    return r.text

def get_url(day, year = 2018):
    url = '/'.join([
        'https://adventofcode.com', str(year), 'day', str(day), 'input'
        ])
    return url

def convert_to_int(input_string, delim='\n'):
    elements = re.split(delim, input_string)
    # remove empty elements, e.g. caused by newlines at eof
    elements = list(filter(None, elements))
    ints = list(map(int, elements))
    return ints