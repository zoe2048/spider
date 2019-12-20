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
            # 为了少请求250个页面，写了下面一段冗杂内容
            # 实际爬取后的数据不应该在此处理
            year_pt = re.compile(r'\d+')
            country_pt = re.compile(r'\d+\s/\s(.*)\s/\s')
            drs_pt = re.compile(r'导演:\s(.*)\s\s\s[主|&nb|&n|&|...]')
            dr_cn = re.compile(r'[\u4e00-\u9fff·]+')
            dr_en = re.compile(r'[^\u4e00-\u9fff·]+')
            info = item['info']
            directors = ''.join(drs_pt.findall(info)).split('/')
            if len(directors) == 1:
                item['director_cn1'], item['director_en1'] = ''.join(dr_cn.findall(directors[0])), ''.join(dr_en.findall(directors[0])).strip()
                item['director_cn2'], item['director_en2'] = '', ''
            elif len(directors) == 2:
                item['director_cn1'], item['director_en1'] = ''.join(dr_cn.findall(directors[0])), ''.join(dr_en.findall(directors[0])).strip()
                item['director_cn2'], item['director_en2'] = ''.join(dr_cn.findall(directors[1])), ''.join(dr_en.findall(directors[1])).strip()
            else:
                item['director_cn1'], item['director_en1'] = '', ''
                item['director_cn2'], item['director_en2'] = '', ''
            countries = ''.join(country_pt.findall(info))
            if countries == '':
                countries = ''.join(re.findall(r'\s/\s(\D+)\s/\s', info))
            couns = countries.split(' ')
            if len(couns) == 1:
                item['country1'], item['country2'], item['country_others'] = couns[0], '', ''
            elif len(couns) == 2:
                item['country1'], item['country2'], item['country_others'] = couns[0], couns[1], ''
            elif len(couns) >= 3:
                item['country1'], item['country2'], item['country_others'] = couns[0], couns[1], couns[2:]
            else:
                item['country1'], item['country2'], item['country_others'] = '', '', '', ''
            item['director'] = ''.join(drs_pt.findall(info))
            item['country'] = countries
            item['year'] = year_pt.search(info).group()
            return item
        elif isinstance(item, ImdbMovieItem):
            countries = item['country']
            couns = countries.split(',')
            if len(couns) == 1:
                item['country1'], item['country2'], item['country_others'] = couns[0], '', ''
            elif len(couns) == 2:
                item['country1'], item['country2'], item['country_others'] = couns[0], couns[1], ''
            elif len(couns) >= 3:
                item['country1'], item['country2'], item['country_others'] = couns[0], couns[1], couns[2:]
            else:
                item['country1'], item['country2'], item['country_others'] = '', '', '', ''
            directors = item['director'].split(',')
            if len(directors) == 1:
                item['director_cn1'], item['director_en1'] = '', directors[0]
                item['director_cn2'], item['director_en2'] = '', ''
            elif len(directors) == 2:
                item['director_cn1'], item['director_en1'] = '', directors[0]
                item['director_cn2'], item['director_en2'] = '', directors[1]
            elif len(directors) == 3:
                item['director_cn1'], item['director_en1'] = '', directors[0]
                item['director_cn2'], item['director_en2'], _ = '', directors[1], directors[2]
            else:
                item['director_cn1'], item['director_en1'] = '', ''
                item['director_cn2'], item['director_en2'] = '', ''
            return item
