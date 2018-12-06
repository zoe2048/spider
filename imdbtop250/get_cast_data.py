# -*- coding:utf8 -*-


import requests
import re
import pymysql
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def get_cast_data(cast):
    for actor in cast:
        actor_data = actor.select_one('td[itemprop="actor"] a')
        person_link = actor_data['href']
        id_pattern = re.compile(r'(?<=nm)\d+(?=/)')
        person_id = int(id_pattern.search(person_link).group())
        actor_name = actor_data.get_text().strip()
        yield {
            'actor_id': person_id,
            'actor_name': actor_name
        }
