# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl douban_movie_top250 -o ../chart/data/doub/doub.csv" .split())
# cmdline.execute("scrapy crawl imdb_movie_top250 -o ../chart/data/imdb/imdb.csv" .split())
