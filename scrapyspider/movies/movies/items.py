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
    director_cn1 = scrapy.Field()
    director_en1 = scrapy.Field()
    director_cn2 = scrapy.Field()
    director_en2 = scrapy.Field()
    country1 = scrapy.Field()
    country2 = scrapy.Field()
    country_others = scrapy.Field()


class ImdbMovieItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    year = scrapy.Field()
    tag = scrapy.Field()
    info = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    director_cn1 = scrapy.Field()
    director_en1 = scrapy.Field()
    director_cn2 = scrapy.Field()
    director_en2 = scrapy.Field()
    country1 = scrapy.Field()
    country2 = scrapy.Field()
    country_others = scrapy.Field()
    runtime = scrapy.Field()
    rated = scrapy.Field()
    year_runtime_rated = scrapy.Field()

