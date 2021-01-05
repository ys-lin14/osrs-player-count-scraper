import numpy as np
import pandas as pd
import requests

from bs4 import BeautifulSoup


def get_osrs_world_select():    
    world_select_url = ('https://oldschool.runescape.com/slu')
    response = requests.get(world_select_url)
    return response


def extract_world_data(response):
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.findAll('tr', {'class':'server-list__row'})
    data = pd.DataFrame(np.array(data, dtype=object))
    return data


def extract_total_player_data(response):
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('p')
    data = pd.DataFrame(data, columns=['player_count'])
    return data


def extract_data(response):
    world_data = extract_world_data(response)
    total_player_data = extract_total_player_data(response)
    return world_data, total_player_data 
