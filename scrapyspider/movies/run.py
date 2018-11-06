# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl imdb_movie_top250 -o test.csv".split())