# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl test -o test.csv".split())