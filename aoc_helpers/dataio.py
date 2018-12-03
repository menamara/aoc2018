import requests
import json
import pkgutil
import os
import re

def load_data(day, year = 2018):
    """ Download and save and return the input for the indicated day.

    Input arguments:
    day -- the day of the calendar for which we want the input as an integer
    year -- the year for which we want the input of the day as an integer 
    The default year is 2018
    
    The data is stored in a subfolder "data/year/".
    The function assumes that this folder already exist.
    The name of the file where the data is stored is "dayday.dat"
    """
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

def split_data(input_string, delim=r'[\n\s,;]'):
    elements = re.split(delim, input_string)
    # remove empty elements, e.g. caused by \n at eof
    elements = list(filter(None, elements))
    return elements


def convert_to_int(input_string, delim=r'[\n\s,;]'):
    elements = split_data( input_string, delim )
    ints = list(map(int, elements))
    return ints