# -*- coding:utf-8 -*-

# settings for scrapyspider->chart

import os


base = os.path.join(os.path.abspath('.'), 'data')


files = {
    '豆瓣': {
        'dir': os.path.join(base, 'doub'),
        'csv': os.path.join(base, 'doub', 'doub.csv'),
    },
    'IMDb': {
        'dir': os.path.join(base, 'imdb'),
        'csv': os.path.join(base, 'imdb', 'imdb.csv'),
    }
}



