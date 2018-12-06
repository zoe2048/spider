import re
#import mysql.connector
import pymysql
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def get_top250_movies_list():
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
    

def store_movie_data_to_db(movie_data):
    print(movie_data)
    sel_sql =  "SELECT * FROM top_250_movies WHERE id =  %d" % (movie_data['movie_id'])
    try:
        cursor.execute(sel_sql)
        result = cursor.fetchall()
    except:
        print("Failed to fetch data")
    if result.__len__() == 0:
        # 添加转义支持电影名带特殊字符的情况如单引号的Schindler's list
        movie_data['movie_name']=pymysql.escape_string(movie_data['movie_name'])
        sql = "INSERT INTO top_250_movies (id, name, year, rate) VALUES ('%d', '%s', '%d', '%f')" % (movie_data['movie_id'], movie_data['movie_name'], movie_data['year'], movie_data['movie_rate'])
        try:
            cursor.execute(sql)
            conn.commit()
            print("movie data ADDED to DB table top_250_movies!")
        except:
            # 发生错误时回滚
            conn.rollback()
    else:
        print("This movie ALREADY EXISTED!!!")

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


def store_director_data_in_db(movie):
    sel_sql = "SELECT * FROM directors  WHERE id =  %d" % (movie['director_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")
    if result.__len__() == 0:
        # 添加转义，支持导演名带单引号的名字
        movie['director_name']=pymysql.escape_string(movie['director_name'])
        sql = "INSERT INTO directors (id, name) VALUES ('%d', '%s')" % (movie['director_id'], movie['director_name'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            print("Director data ADDED to DB table directors!", movie['director_name'] )
        except:
            # 发生错误时回滚
            conn.rollback()
    else:
        print("This Director ALREADY EXISTED!!")

    sel_sql = "SELECT * FROM direct_movie  WHERE director_id =  %d AND movie_id = %d" % (movie['director_id'], movie['movie_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO direct_movie (director_id, movie_id) VALUES ('%d', '%d')" % (movie['director_id'], movie['movie_id'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            print("Director direct movie data ADD to DB table direct_movie!")
        except:
            # 发生错误时回滚
            conn.rollback()
    else:
        print("This Director direct movie ALREADY EXISTED!!!")


def store_actor_data_to_db(actor, movie):
    sel_sql = "SELECT * FROM actors WHERE id =  %d" % (actor['actor_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        #转义特殊字符
        actor['actor_name']=pymysql.escape_string(actor['actor_name'])
        sql = "INSERT INTO actors  (id, name) VALUES ('%d', '%s')" % (actor['actor_id'], actor['actor_name'])

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            print("actor data ADDED to DB table actors!")
        except:
            # 发生错误时回滚
            conn.rollback()
    else:
        print("This actor has been saved already")

    sel_sql = "SELECT * FROM cast_in_movie WHERE actor_id =  %d AND movie_id = %d" % (actor['actor_id'], movie['movie_id'])
    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO cast_in_movie (actor_id, movie_id)  VALUES ('%d', '%d')" % (actor['actor_id'], movie['movie_id'])

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            print("actor casted in movie data ADDED to DB table cast_in_movie!")
        except:
            # 发生错误时回滚
            conn.rollback()
    else:
        print("This actor casted in movie data ALREADY EXISTED")


def main():
    try:
        for movie in get_top250_movies_list():
            store_movie_data_to_db(movie)
            get_movie_detail_data(movie)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    #conn=mysql.connector.connect(host='192.168.99.100',port='3306',user='root',password='admin',database='imdb_movies')
    conn=pymysql.connect(host='192.168.99.100',port=3306,user='root',password='admin',database='imdb_movies',charset='utf8')
    cursor=conn.cursor()
    main()
