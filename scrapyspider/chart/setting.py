# -*- coding:utf-8 -*-

# settings for scrapyspider->chart

import os


basepath = os.path.join(os.path.abspath('.'), 'data')
htmlpath = os.path.join(os.path.abspath('.'), 'html')


# 要从csv提取数据的列名
names = {
    'doub': ['country', 'year'],
    'imdb': ['country', 'year']
         }

