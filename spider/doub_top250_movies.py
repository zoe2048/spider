import re
import pymysql
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, HTTPError


def filter_data(nm, fname, string):
    """
    处理字符串
    :param nm: 处理类型
    :param fname: 函数代码
    :param string: 待处理的字符串
    :return: 处理后的字符串
    """
    if nm == 'sub':
        if fname == '1':
            newstring = re.sub(r'\xa0/\xa0', '', string)
    if nm == 'split':
        if fname == '1':
            newstring = re.split(r'  /  ', string)
    if nm == 'search':
        if fname == '1':
            newstring = re.search(r'\d+', string).group()
    if nm == 'replace':
        if fname == '1':
            newstring = (string.replace('\n', '')).strip()
    return newstring


# 处理同个文档树路径下，标签个数不一致，获取数据问题
def deal_data(fname, datatype, data):
    if fname == '1':
        if datatype == 'name':
            if len(data) == 3:
                data1, data2, data3 = data[0].text, data[1].text, data[2].text
            elif len(data) == 2:
                data1, data2, data3 = data[0].text, '', data[1].text
            else:
                raise NameError
            return data1, data2, data3
        if datatype == 'others':
            if len(data) == 2:
                data1, data2 = data[0], data[1]
            elif len(data) == 1:
                data1, data2 = data[0], ''
            elif len(data) == 0:
                data1, data2 = '', ''
            else:
                raise NameError
            return data1, data2


def get_top250_movies_list(url="https://movie.douban.com/top250"):
    headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            movies = soup.select('ol[class="grid_view"] > li')
            for movie in movies:
                ranking = movie.select_one('.item>.pic>em').get_text()
                posterlink = movie.select_one('.pic img')['src']
                name = movie.select('.info>.hd >a>span')
                movielink = movie.select_one('.info>.hd>a')['href']
                movieinfo = movie.select_one('.info>.bd>p').get_text()
                ratinginfo = movie.select('.info>.bd>.star>span')
                try:
                    quote = movie.select_one('.info>.bd>.quote>.inq').get_text()
                except AttributeError:
                    quote = ''
                ratingscore = ratinginfo[1].text
                ratingnum = filter_data('search', '1', ratinginfo[3].text)
                info = filter_data('replace', '1', movieinfo)
                name1, name2, name3 = deal_data('1', 'name', name)
                name_cn = name1
                name_en = filter_data('sub', '1', name2)
                name_other = filter_data('sub', '1', name3)
                name_others = filter_data('split', '1', name_other)
                other1, other2 = deal_data('1', 'others', name_others)
                yield {
                    'movie_id': int(ranking),
                    'movie_name_cn': name_cn,
                    'movie_name_en': name_en,
                    'movie_name_other1': other1,
                    'movie_name_other2': other2,
                    'movie_info': info,
                    'movie_ratingscore': ratingscore,
                    'movie_ratingnum': int(ratingnum),
                    'movie_quote': quote,
                    'movie_poster': posterlink,
                    'movie_link': movielink,
                }
        else:
            raise HTTPError
    except RequestException:
        raise


def create_urls():
    baseurl = "https://movie.douban.com/top250?start="
    endurl = "&filter="
    return (''.join(baseurl + str(page) + endurl) for page in [n*25 for n in range(10)])


def store_movies_data(urls):
    for url in urls:
        movie_data_g = get_top250_movies_list(url)
        for movie_data in movie_data_g:
            movie_data['movie_name_en'] = pymysql.escape_string(movie_data['movie_name_en'])
            movie_data['movie_name_other1'] = pymysql.escape_string(movie_data['movie_name_other1'])
            movie_data['movie_name_other2'] = pymysql.escape_string(movie_data['movie_name_other2'])
            movie_data['movie_quote'] = pymysql.escape_string(movie_data['movie_quote'])
            movie_data['movie_info'] = pymysql.escape_string(movie_data['movie_info'])
            sql = """INSERT INTO douban (id, name_cn, name_en, name_other1, name_other2, info, score, ratingnum,
               quote, poster, link) VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s')""" % \
                  (movie_data['movie_id'], movie_data['movie_name_cn'], movie_data['movie_name_en'],
                   movie_data['movie_name_other1'], movie_data['movie_name_other2'], movie_data['movie_info'],
                   movie_data['movie_ratingscore'], movie_data['movie_ratingnum'], movie_data['movie_quote'],
                   movie_data['movie_poster'], movie_data['movie_link'])
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception:
                conn.rollback()


def main():
    try:
        urls = create_urls()
        store_movies_data(urls)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    conn = pymysql.connect(host='192.168.99.100', port=3306, user='root', password='admin', database='imdb_movies', charset='utf8')
    cursor = conn.cursor()
    main()
