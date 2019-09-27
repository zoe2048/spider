# -*- coding:utf8 -*-


import requests
import re
import pymysql
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_top250_movies_list():
    """
    获取电影海报、分数、详情链接、上映年份、电影名、电影id信息
    movie_id:通过在页面获取的数字做为电影信息表的id
    """
    url = "http://www.imdb.com/chart/top"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            movies = soup.select('tbody tr')
            for movie in movies:
                poster = movie.select_one('.posterColumn')
                score = poster.select_one('span[name="ir"]')['data-value']
                movie_link = movie.select_one('.titleColumn').select_one('a')['href']
                year_str = movie.select_one('.titleColumn').select_one('span').get_text()
                year_pattern = re.compile('\d{4}')
                year = int(year_pattern.search(year_str).group())
                id_pattern = re.compile(r'(?<=tt)\d+(?=/?)')
                movie_id = int(id_pattern.search(movie_link).group())
                movie_name = movie.select_one('.titleColumn').select_one('a').string

                yield {
                    'movie_id': movie_id,
                    'movie_name': movie_name,
                    'year': year,
                    'movie_link': movie_link,
                    'movie_rate': float(score)
                }
        else:
            print("Error when request URL")
    except RequestException:
        print("Request Failed")
        return None
