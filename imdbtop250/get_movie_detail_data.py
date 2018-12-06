import requests
import re
import pymysql
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_movie_detail_data(movie_data):
    url = "http://www.imdb.com" + movie_data['movie_link']
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            # Parse Director's info
            director = soup.select_one('span[itemprop="director"]')
            person_link = director.select_one('a')['href']
            director_name = director.select_one('span[itemprop="name"]')
            id_pattern = re.compile(r'(?<=nm)\d+(?=/?)')
            person_id = int(id_pattern.search(person_link).group())
            movie_data['director_id'] = person_id
            movie_data['director_name'] = director_name.string
            store_director_data_in_db(movie_data)
            #parse Cast's data
            cast = soup.select('table.cast_list tr[class!="castlist_label"]')
            for actor in get_cast_data(cast):
                store_actor_data_to_db(actor, movie_data)
        else:
            print("GET url of movie Do Not 200 OK!")
    except RequestException:
        print("Get Movie URL failed!")
        return None
