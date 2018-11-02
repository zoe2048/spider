# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评分人数
    score_num = scrapy.Field()
    # 电影类型
    tag = scrapy.Field()

class ImdbMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评分人数
    # 电影类型
    tag = scrapy.Field()
