# -*- coding:utf-8 -*-

# settings for scrapyspider->chart

import os


basepath = os.path.join(os.path.abspath('.'), 'data')


doub = {
    "doub_path": os.path.join(basepath, 'doub'),
    "doub_csv":  os.path.join(basepath, 'doub', 'doub.csv'),
    "cfilenm": os.path.join(basepath, 'doub', 'country.txt'),
    "yfilenm": os.path.join(basepath, 'doub', 'year.txt'),

}

imdb = {
    "imdb_path": os.path.join(basepath, 'imdb'),
    "imdb_csv":  os.path.join(basepath, 'imdb', 'imdb.csv'),
    "cfilenm": os.path.join(basepath, 'imdb', 'country.txt'),
    "yfilenm": os.path.join(basepath, 'imdb', 'year.txt'),
}
