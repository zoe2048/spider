# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()  # 排名
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    year = scrapy.Field()
    info = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()


class ImdbMovieItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    year = scrapy.Field()
    tag = scrapy.Field()
    info = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()

