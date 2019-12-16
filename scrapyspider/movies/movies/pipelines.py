# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from movies.items import DoubanMovieItem, ImdbMovieItem


class MoviesPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DoubanMovieItem):
            year_pt = re.compile(r'\d+')
            country_pt = re.compile(r'\d+\s/\s(.*)\s/\s')
            dirc_pt = re.compile(r'导演:\s(.*)\s\s\s主演')
            info = item['info']
            item['year'] = year_pt.search(info).group()
            item['director'] = ''.join(dirc_pt.findall(info))
            item['country'] = ''.join(country_pt.findall(info))
            if item['country'] == '':
                item['country'] = ''.join(re.findall(r'\s/\s(\D+)\s/\s', info))
            return item
        elif isinstance(item, ImdbMovieItem):
            return item
