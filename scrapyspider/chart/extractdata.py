# -*- coding:utf-8 -*-

"""
爬虫爬取的数据，保存到csv文件中提取出制片国家/地区的数据
并保存到txt文件供制片国家/地区电影数分布数据可视化使用
"""

import os
import csv

basepath = os.path.abspath('.')
datapath = os.path.join(basepath, 'data')
doubfilenm = 'doub'
imdbfilenm = 'imdb'
doubpath = os.path.join(datapath, doubfilenm)
imdbpath = os.path.join(datapath, imdbfilenm)
doubcsvpath = os.path.join(doubpath, 'douban.csv')
imdbcsvpath = os.path.join(imdbpath, 'imdb.csv')


def extract_country(infile):
    if 'doub' in infile:
        with open(infile, newline='') as f:
            next(f)
            reader = csv.reader(f)
            for row in reader:
                tag = row[4]
                countrysp = tag.split('?/?')
                country = countrysp[1]
                yield country
    elif 'imdb' in infile:
        with open(infile, newline='') as f:
            next(f)
            reader = csv.reader(f)
            for row in reader:
                country = row[1]
                yield country


def writecountrytotxt(indata, outfile):
    with open(outfile, 'a+', encoding='utf-8-sig') as f:
        for c in indata:
            f.write(c + '\n')


if __name__=='__main__':
    doubc = extract_country(doubcsvpath)
    imdbc = extract_country(imdbcsvpath)
    doubcountry = os.path.join(doubpath, 'country.txt')
    imdbcountry = os.path.join(imdbpath, 'country.txt')
    if os.path.exists(doubcountry):
        os.remove(doubcountry)
    if os.path.exists(imdbcountry):
        os.remove(imdbcountry)
    writecountrytotxt(doubc, doubcountry)
    writecountrytotxt(imdbc, imdbcountry)






