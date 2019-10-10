# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birth = scrapy.Field()
    country = scrapy.Field()
    bio = scrapy.Field()
